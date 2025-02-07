from langchain_huggingface import HuggingFaceEndpoint, HuggingFaceEmbeddings
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader, UnstructuredFileLoader, UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
import textwrap
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence
from api.models import WebpageSummary, YoutubeVideoSummary
from bs4 import BeautifulSoup
import requests
from langchain.chains import RetrievalQAWithSourcesChain, LLMChain
from django.contrib.auth.models import User
from celery import shared_task

# Loading LLM
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
)



# Splitting Docs
def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs


# def summarize_content(docs):
#     chain = load_summarize_chain(llm, chain_type="refine")
#     result = chain.invoke(split_docs)

#     return result["output_text"]


def summarize_content(docs):
    # Define prompt
    prompt_template = """
    Write a detailed summary of the following:
    "{text}"
    DETAILED SUMMARY:
    """
    prompt = PromptTemplate.from_template(prompt_template)
    summarizing_chain = prompt | llm | StrOutputParser()
    # Define LLM chain
    # llm_chain = LLMChain(llm=llm, prompt=prompt)
    # # Define StuffDocumentsChain
    # stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")
    result = summarizing_chain.invoke({ "text": docs })

    return result

# Loading Web Pages
@shared_task()
def load_web_page(link, user):
    try:
        loader = WebBaseLoader(link)
        documents = loader.load()
        docs = split_docs(documents)
        r = requests.get(link) 
        soup = BeautifulSoup(r.content, 'html.parser')
        site_title = soup.title.string
        try:
            result = summarize_content(docs)
        except:
            print("Unable to Summarize")
        webpagesummary_model = WebpageSummary(name=site_title, user=User.objects.get(id=user), link=link, summary=result)
        # vectorstore = Chroma.from_documents(collection_name="bootstrap_docs", documents=docs, embedding=HuggingFaceEmbeddings(), persist_directory=f"./chroma_db/{user.username}/{webpagesummary_model.summary_id}")
        # print(vectorstore.get(["ids", "embeddings", "metadatas", "documents"]))
        webpagesummary_model.save()
        
        return webpagesummary_model.summary_id
    except:
        return "Unable to load or summarize webpage :sob:"


@shared_task()
def load_youtube_video(link, user):
    video_id = YoutubeLoader.extract_video_id(link)
    loader = YoutubeLoader.from_youtube_url(link,
        add_video_info=True,
        language=["en", "hi"],
        translation="en")
    documents = loader.load()
    docs = split_docs(documents)
    title = documents[0].metadata["title"]
    result = summarize_content(docs)
    youtubevideosummary_model = YoutubeVideoSummary(name=title, video_id=video_id, user=User.objects.get(id=user), summary=result)
    youtubevideosummary_model.save()
    # vectorstore = Chroma.from_documents(documents=docs, embedding=HuggingFaceEmbeddings(),  persist_directory="./chroma_db")

    return youtubevideosummary_model.summary_id



def load_document(url, user):
    loader = UnstructuredURLLoader(url)
    documents = loader.load()
    docs = split_docs(documents)
    result = summarize_content(docs)



def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def answer_question(user, summaryid, question):
    # Retrieve and generate using the relevant snippets of the blog.
    docs = Chroma(collection_name="bootstrap_docs", persist_directory=f"./chroma_db/{user.username}/{summaryid}", embedding_function=HuggingFaceEmbeddings())
    retriever = docs.as_retriever()
    prompt = hub.pull("rlm/rag-prompt")

    chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm, # OpenAI default (gpt-3.5), with low t for more deterministic output
        chain_type="stuff", # LangChain provides shortcuts with prefilled prompts
        retriever=retriever, # Use the chroma DB to check for results
        chain_type_kwargs={"verbose": True}  # Log everything
    )

    result = chain({"question": question}, return_only_outputs=True)
    print(result)
    return result