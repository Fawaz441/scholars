var arrow = document.querySelector(".arrow_down");
if(arrow){
window.addEventListener("scroll",function(){
    if (window.scrollY > 0){
        arrow.classList.add("fade_arrow");
    }
    else{
        arrow.classList.remove("fade_arrow");
    }
})}

// Sliding
var slideIndex = 0;
var colorIndex = 0;
showSlides();
color()

function showSlides(){
    var i;
    var slides = document.querySelectorAll(".slide");
    for(i=0;i<slides.length;i++){
        slides[i].style.display="none";
    }
 
   

    slideIndex++;
    if(slideIndex > slides.length){slideIndex=1}
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides,5000);

}


function color(){
    var dots = document.querySelectorAll(".dot");

    for(i=0;i<dots.length;i++){
        dots[i].classList.remove("active");
    }
    colorIndex++;
    if(colorIndex > dots.length){colorIndex=1}
    dots[colorIndex - 1].classList.add("active");
    setTimeout(color,5000);
}