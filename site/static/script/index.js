gsap.fromTo(".header", {opacity: 0, y: -20, delay: 2}, {opacity: 1, y: 0, duration: 1, ease: "power1.out"});

gsap.fromTo(".tagline", {opacity: 0, y: 40, delay: 4}, {opacity: 1, y: 0, duration: 2, ease: "sine.out"});

const boxes = gsap.utils.toArray('.box');
boxes.forEach(box => {
  gsap.set(box, {opacity: 0, y: 40});
  gsap.to(box, {
    opacity: 1,
    y: 0,
    ease: "expo",
    duration: 1,
    immediateRender: false,
    scrollTrigger: {
        trigger: box,
        scrub: true,
        start: "-100px +=200px",
        end: "0px"
      }
  })
});


const subboxes = gsap.utils.toArray('.subbox');
subboxes.forEach(box => {
  gsap.set(box, {opacity: 0, y: 40});
  gsap.to(box, {
    opacity: 1,
    y: 0,
    ease: "power4.out",
    duration: 1,
    immediateRender: false,
    scrollTrigger: {
        trigger: box,
        scrub: true,
        start: "-=100px +=200px",
        end: "0px"
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
            start: `-=200px +=100px`,
            end: `-=100px +=150px`
          }
    })
  });
