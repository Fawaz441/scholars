try{
    var ads_dropdown_initator = document.querySelector(".ads");
    var ads_dropdown = document.querySelector(".children");
    
    ads_dropdown_initator.addEventListener("mouseover",function(){
        ads_dropdown.style.display = "block";
    })
    
    ads_dropdown.addEventListener("mouseleave",function(){
        ads_dropdown.style.display = 'none';
    })
}
catch{
    console.log('%c Ham not Found','color:#fff;font-size:3rem')
}



var ham = document.getElementById("nav_small");
ham.addEventListener("click",function(){
    this.classList.toggle("expanded");
})

// var spans = document.querySelectorAll("#nav-icon2 span");
// spans.forEach((one) => {
//     one.addEventListener("click",function(){
//         ham.classList.toggle("open");
//     })
// })


