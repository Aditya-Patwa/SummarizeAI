gsap.fromTo(".header", { opacity: 0, y: -20, delay: 2 }, { opacity: 1, y: 0, duration: 1, ease: "power1.out" });


let openNav = document.getElementById("openNav");
let closeNav = document.getElementById("closeBtn");

const tl = gsap.timeline({paused: true });
// tl.add(() => {
//     document.getElementsByClassName("navbar")[0].classList.replace("grid", "hidden");
// }, 0)
// tl.add(() => {
//     document.getElementsByClassName("navbar")[0].classList.replace("hidden", "grid");
// }, 0)
// tl.to(".navbar", {
//     opacity: 0
// });

// tl.to(".navbar", {
//     opacity: 1,
//     duration: .1,
//     ease: "sine.out"
// });

tl.to(".navbar", {
    right: 0,
    duration: 1,
    ease: "power3.out"
})

tl.to('.sidebar', {
    width: window.innerWidth,
    duration: .5,
    ease: "power4.out"
})

const navitem = gsap.utils.toArray('.navitem');
navitem.forEach(item => {

  tl.fromTo(item, {
    opacity: 0,
    x: 20
  }, {
    opacity: 1,
    x: 0,
    ease: "power4.out",
    duration: .35
  })
});

openNav.addEventListener("click", () => {
    tl.play();
});


closeNav.addEventListener("click", () => {
    tl.reverse();
});

