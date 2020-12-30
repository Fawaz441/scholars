TweenMax.to('.image svg',1,{
    scale:1,
    opacity:1,
    ease: "elastic.inOut(1.5, 1)",
})
TweenMax.to("#bino,#fillhand,#fillhand_outline",2,{y:-40,delay:1,yoyo:true,repeat:-1,
ease:'power1.inOut'
})
