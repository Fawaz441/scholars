// const TypeWriter = function(txtElement,words,wait=3000){
//     this.txtElement = txtElement;
//     this.words = words;
//     this.txt = '';
//     this.wordIndex = 0;
//     this.wait = parseInt(wait,10);
//     this.type();
//     this.isDeleting = false;
// }

// // Type method
// TypeWriter.prototype.type = function(){
//     // Current Index of word
//     const current = this.wordIndex % this.words.length;
//     // Get full text of current word
//     const fulltxt = this.words[current];
//     // Check if deleting
//     if(this.isDeleting){
//         // Remove char
//         this.txt = fulltxt.substring(0, this.txt.length - 1);
        
//     }else{
//         // add char
//         this.txt = fulltxt.substring(0, this.txt.length + 1);
//     }
//     // insert text into element
//     this.txtElement.innerHTML=`<span class="txt">${this.txt}</span>`;
//     // Type speed
//     let typeSpeed = 300;
//     if(this.isDeleting){
//         typeSpeed /= 2; 
//     }
//     // If word is complete
//     if(!this.isDeleting && this.txt === fulltxt){
//         // Make pause at end
//         typeSpeed = 1000;
//         // Set delete to true
//         this.isDeleting = true;
//     } else if(this.isDeleting && this.txt === ''){
//         this.isDeleting = false;
//         // Move to next word
//         this.wordIndex++;
//         // Pause before start typing
//         typeSpeed = 500;
//     }
    
//     setTimeout(() => this.type(),typeSpeed);
// }
// // INIT on DOm LOAD

// document.addEventListener("DOMContentLoaded",init);
// // init function
// function init(){
//     const txtElement = document.querySelector('.changer');
//     const words = JSON.parse(txtElement.getAttribute('data-words'));
//     const wait = txtElement.getAttribute('.data-wait'); 
//     new TypeWriter(txtElement,words,wait);
// }



function scrollwindow(){
    var windowHeight = window.innerHeight / 1.2;
    var materials_text = document.querySelectorAll(".down");
    for(var i=0;i<materials_text.length;i++){
        var limit = materials_text[i].getBoundingClientRect().top;
        if( limit < windowHeight ){
            materials_text[i].classList.add('show')
        }}
    }
    
    window.addEventListener("scroll",scrollwindow);
    
    
    let tl1 = new TimelineMax();

    tl1.from(".header_intro h1",1,{
        scale:0,
        opacity:0,
        x:500,
        ease:'power.inOut',
    })
    tl1.from(".header_intro p",1,{
        scale:0,
        opacity:0,
        y:40,
        ease:'elastic.inOut(1.5, 1)',
        transformOrigin:'50% center'
    })
    
    tl1.from(".join_cta",1,{
        scale:0,
        opacity:0,
        x:-20,
        ease:'elastic.inOut(1.5, 1)',
        // transformOrigin:'100% 50%'
        delay:-0.6
    })
    
    tl1.from(".materials_cta",0.4,{
        scale:0,
        opacity:0,
        x:40,
        ease:'elastic.inOut(1.5, 1)',
        // transformOrigin:'0% 50%'
        delay:-0.2,
    })
    // TweenMax.saveStyles();
    tl1.from(".arrow_down",0.4,{
        opacity:0,
    })




    const orangey = document.querySelector(".orangey");
    const header = document.querySelector('header');
  

            let tl2 = new TimelineMax();
            tl2.to(header,1,{
                // y:"-50vh",
            })
            tl2.to(".arrow_down",0.2,{
                autoAlpha:0,
            })
            tl2.to(".orangey",4,{
                yPercent:-180,
                // delay:-1.8,
                // ease:Expo.easeInOut,
            })
            // tl2.to(".orangey",4,{
            //     // yPercent:-70,
            //     // delay:-1.8,
            //     ease:Expo.easeInOut,
            // })
            tl2.to("#binocular .st4",2,{
                y:5,
                ease:Power2.easeInOut,
                yoyo:true,
                repeat:3,
            })
            ScrollTrigger.create({
                // trigger:'.orangey',
                scrub:1,
                animation:tl2,
            })
  
