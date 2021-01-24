
document.addEventListener('DOMContentLoaded', () => {


    var scrollLeft = document.querySelector(".scroll-left");
    var scrollRight = document.querySelector(".scroll-right");
    var adverts = document.querySelector(".adverts_wrapper");

    // var scrollLeft1 = document.querySelector(".scroll-left1");
    // var scrollRight1 = document.querySelector(".scroll-right1");
    // var adverts1 = document.querySelector(".adverts_wrapper1");

    // var scrollLeft2 = document.querySelector(".scroll-left2");
    // var scrollRight2 = document.querySelector(".scroll-right2");
    // var adverts2 = document.querySelector(".adverts_wrapper2");

    scrollLeft.addEventListener("click", function () {
        adverts.scrollLeft -= 100;
    })

    scrollRight.addEventListener("click", function () {
        adverts.scrollLeft += 100;
    })



    // scrollLeft1.addEventListener("click", function () {
    //     adverts1.scrollLeft -= 100;
    // })

    // scrollRight1.addEventListener("click", function () {
    //     adverts1.scrollLeft += 100;
    // })



    // scrollLeft2.addEventListener("click", function () {
    //     adverts2.scrollLeft -= 100;
    // })

    // scrollRight2.addEventListener("click", function () {
    //     adverts2.scrollLeft += 100;
    // })

    const links = document.querySelectorAll(".add_stuff a");
    links.forEach(btn => {
        btn.addEventListener("click", function (e) {
            let x = e.clientX - e.target.offsetLeft;
            let y = e.clientY - e.target.offsetTop;
            let ripples = document.createElement("span");
            ripples.style.left = x + 'px';
            // ripples.style.top = y +'px';
            ripples.className = 'white_overlay';
            this.appendChild(ripples);
            setTimeout(() => {
                ripples.remove()
            }, 400);
        })
    })

    const backdrop = document.querySelector(".backdropx");
    var formBackdrop = document.querySelector(".form_backdrop");
    var formContainer = document.querySelector(".form_container");
    var exiter = document.querySelector(".form_container .exit");
    var schoolForm = document.querySelector(".school_form")
    var materialForm = document.querySelector(".material_form")
    var pqForm = document.querySelector(".pq_form")
    var courseForm = document.querySelector(".course_form")
    // var coverer = document.querySelectorAll('.form_backdrop')
    // if (coverer.length > 0){
    //     coverer[0].addEventListener('click',() => {
    //         formContainer.classList.remove('form-slide-down')
    //         coverer[0].classList.remove('form-backdrop-display')
    //     })
    // }

    function bringSchool() {
        backdrop.classList.add("backdrop-display");
        formBackdrop.classList.add("form-backdrop-display");
        formContainer.classList.add("form-slide-down");
        schoolForm.classList.add("show");
    }
    function bringMaterial() {
        backdrop.classList.add("backdrop-display");
        formBackdrop.classList.add("form-backdrop-display");
        formContainer.classList.add("form-slide-down");
        materialForm.classList.add("show");
    }
    function bringPq() {
        backdrop.classList.add("backdrop-display");
        formBackdrop.classList.add("form-backdrop-display");
        formContainer.classList.add("form-slide-down");
        pqForm.classList.add("show");
    }
    function bringCourse() {
        backdrop.classList.add("backdrop-display");
        formBackdrop.classList.add("form-backdrop-display");
        formContainer.classList.add("form-slide-down");
        courseForm.classList.add("show");
    }

    function exitForm() {
        backdrop.classList.remove("backdrop-display");
        formBackdrop.classList.remove("form-backdrop-display");
        formContainer.classList.remove("form-slide-down");
        courseForm.classList.remove("show");
        pqForm.classList.remove("show");
        materialForm.classList.remove("show");
        schoolForm.classList.remove("show");
    }

    function cleanit() {

        console.log("Hello");
        for (let i = 0; i < inputs.length; i++) {
            inputs[i].value = '';
        }
    }

    window.onload = () => {
        var inputs = document.querySelectorAll("input[type='text']");
        console.log(inputs.length);
        for (let i = 0; i < inputs.length; i++) {
            inputs[i].value = '';
        }
    };



    let schools = document.querySelector(".schools");
    let school_btn = document.querySelector(".check_school_courses a h3");
    school_btn.addEventListener("click", function () {
        backdrop.classList.add("backdrop-display");
        schools.classList.add('showingall')
    })

    let materials = document.querySelector(".materials");
    let material_btn = document.querySelector(".mater");
    material_btn.addEventListener("click", function () {
        backdrop.classList.add("backdrop-display");
        materials.classList.add('showingall')
    })

    let new_adverts = document.querySelector(".new_adverts");
    let new_adverts_btn = document.querySelector(".check_adverts a h3");
    new_adverts_btn.addEventListener("click", function () {
        backdrop.classList.add("backdrop-display");

        new_adverts.classList.add('showingall')

    })

    let new_materials = document.querySelector(".new_materials");
    let new_materials_btn = document.querySelector(".check_materials a h3");
    new_materials_btn.addEventListener("click", function () {
        backdrop.classList.add("backdrop-display");

        new_materials.classList.add('showingall')
        
    })

    let new_pqs = document.querySelector(".new_pqs");
    let new_pqs_btn = document.querySelector(".check_pqs a h3");
    new_pqs_btn.addEventListener("click", function () {
        backdrop.classList.add("backdrop-display");

        new_pqs.classList.add('showingall')
    })

    var exiters = document.querySelectorAll(".close_modal");
    exiters.forEach((closer) => {
        closer.addEventListener("click", () => {
            backdrop.classList.remove("backdrop-display");
            closer.parentElement.classList.remove('showingall')
            // closer.parentElement.style.bottom = '120%';

        })
    })

    let materialx = document.getElementById('material')
    let pqx = document.getElementById('pq')
    let schoolx = document.getElementById('school')
    let coursex = document.getElementById('course')
    let formExiter = document.getElementById('formexit')

    materialx.addEventListener('click',bringMaterial)
    pqx.addEventListener('click',bringPq)
    schoolx.addEventListener('click',bringSchool)
    coursex.addEventListener('click',bringCourse)
    formExiter.addEventListener('click',exitForm)

})