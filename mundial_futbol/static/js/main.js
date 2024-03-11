document.getElementById("crear").addEventListener("click", function(){
    var cont = document.getElementById("container_equipo");

    cont.classList.toggle("container_of");
    cont.classList.toggle("container_on");
    
});

document.getElementById("crear").addEventListener("click", function(){
    var contJ = document.getElementById("container_jugadores");

    contJ.classList.toggle("container_of");
    contJ.classList.toggle("container_on");
});

document.getElementById("crear").addEventListener("click", function(){
    var cont = document.getElementById("container_posiciones");

    cont.classList.toggle("container_of");
    cont.classList.toggle("container_on");
});

document.getElementById("crear").addEventListener("click", function(){
    var cont = document.getElementById("container_tecnicos");

    cont.classList.toggle("container_of");
    cont.classList.toggle("container_on");
});

let slideIndex = 0;
showSlide(slideIndex);

function showSlide(n) {
    const slides = document.querySelector('.carousel-inner');
    const slideWidth = slides.children[0].offsetWidth;
  slides.style.transform = `translateX(${-n * slideWidth}px)`;
}

function prevImage() {
    if (slideIndex > 0) {
        slideIndex--;
    } else {
        slideIndex = document.querySelectorAll('.carousel-inner img').length - 1;
    }
    showSlide(slideIndex);
}

function nextImage() {
    if (slideIndex < document.querySelectorAll('.carousel-inner img').length - 1) {
        slideIndex++;
    } else {
        slideIndex = 0;
    }
    showSlide(slideIndex);
}
