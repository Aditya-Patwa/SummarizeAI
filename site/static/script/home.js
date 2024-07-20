gsap.fromTo(".tagline", { opacity: 0, y: 40, delay: 4 }, { opacity: 1, y: 0, duration: 1, ease: "sine.out" });

const boxes = gsap.utils.toArray('.box');
boxes.forEach(box => {
  gsap.set(box, { opacity: 0, y: 40 });
  gsap.to(box, {
    opacity: 1,
    y: 0,
    ease: "expo",
    duration: 1,
    immediateRender: false,
    scrollTrigger: {
      trigger: box,
      scrub: true,
      start: "top center",
      end: "center center"
    }
  })
});


const subboxes = gsap.utils.toArray('.subbox');
subboxes.forEach(box => {
  gsap.set(box, { opacity: 0, y: 40 });
  gsap.to(box, {
    opacity: 1,
    y: 0,
    ease: "power4.out",
    duration: 1,
    immediateRender: false,
    scrollTrigger: {
      trigger: box,
      scrub: true,
      start: "top center",
      end: "center center"
    }
  })
});


const balls = gsap.utils.toArray('.entertext');
balls.forEach(ball => {
  gsap.set(ball, {
    opacity: 0,
    y: 30,
  })

  gsap.to(ball, {
    opacity: 1,
    y: 0,
    ease: "none",
    immediateRender: false,
    scrollTrigger: {
      trigger: ball,
      scrub: true,
      start: `top center`,
      end: `bottom center`,
    }
  })
});


// const fadeentertext = gsap.utils.toArray('.fadeentertext');
// fadeentertext.forEach(ball => {
//   gsap.set(ball, {
//     opacity: 1,
//     y: 30,
//   })

//   gsap.to(ball, {
//     opacity: 1,
//     y: 0,
//     ease: "none",
//     immediateRender: false,
//     scrollTrigger: {
//       trigger: ball,
//       scrub: true,
//       start: `top center`,
//       end: `bottom center`,
//       markers: true,
//       pin: true,
//     }
//   })
// });


const fadeentertext = gsap.utils.toArray('.fadeentertext');
fadeentertext.forEach(text => {
  gsap.set(text, {
    // y: 50,
    opacity: 0
  })
  
  
  gsap.to(text, {
    // y: 0,
    color: "pink",
    opacity: 1,
    ease: "sine.out",
    immediateRender: true,
    scrollTrigger: {
      trigger: text,
      scrub: true,
      start: `top-=100px center`,
      end: `bottom center`
    }
  });
});


gsap.set(".fadeentertextbottom", {
  // y: 50,
  opacity: 0
})


gsap.to(".fadeentertextbottom", {
  // y: 0,
  opacity: 1,
  ease: "sine.out",
  immediateRender: true,
  scrollTrigger: {
    trigger: ".fadeentertextbottom",
    scrub: true,
    start: `top+=${window.innerHeight/2} center`,
    end: `center+=${window.innerHeight/2} center`
  }
});



gsap.to(".introduction", {
  scrollTrigger: {
    trigger: ".introduction",
    start: `top center`,
    end: `bottom center`,
    scrub: true,
    onUpdate: self => {
      let myDiv = document.getElementsByClassName("introduction")[0];
      let text = myDiv.textContent.trim();

      const point = Math.ceil(text.length*self.progress);
      const words = text.substring(0, point);
      const remainingWords = text.substring(point);

      const readSpan = document.createElement('span');
      readSpan.textContent = words;
      readSpan.classList.add("text-white");

      const remainingSpan = document.createElement('span');
      remainingSpan.textContent = remainingWords;

      myDiv.innerHTML = "";
      myDiv.appendChild(readSpan);
      myDiv.appendChild(remainingSpan);
    }
  }
})



gsap.set(".backcover", {
  height: 0
});

gsap.to(".backcover", {
  height: window.innerHeight,
  ease: "none",
  immediateRender: false,
  scrollTrigger: {
    trigger: ".backcovermove",
    scrub: true,
    start: `center center`,
    end: `bottom center`,
    pin: true
  }
});



gsap.set(".faqs", {
  opacity: 0,
  y: 50
});

gsap.to(".faqs", {
  y: 0,
  opacity: 1,
  ease: "sine.out",
  immediateRender: false,
  scrollTrigger: {
      trigger: ".backcovermove",
      scrub: true,
      start: `top+=${window.innerHeight*2.2} center`,
      end: `top+=${window.innerHeight*2.55} center`
  }
})

