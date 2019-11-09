/* 
Scaling image animation js

Light box modal js

*/ 

var navBar = document.querySelector('.desktop-nav');
const windowWidth = window.innerWidth;
var lightboxModal = document.querySelector('.lightbox-modal');
var closeBtn = document.querySelector('.close-btn');
var thumbnailControlsImages = Array.from(document.getElementsByClassName("thumbnail-controls-images"));
var mySlides = Array.from(document.getElementsByClassName('mySlides'));
var openModalImg = Array.from(document.getElementsByClassName("open-modal-img"));
var slideIndex = 1;


let imageThumbs = document.getElementsByClassName('collection-detail-image');
let imageThumbsArray= [];
let scaleAmount = 1.30;
let resetAmount = 1;

function myEvents (imageThumbs) {
        for (i=0;i<imageThumbs.length;i++) {

            // Event listener for the lightbox
            imageThumbs[i].addEventListener("click", openModal );

            // Event listeners for the thumbnail animations
            imageThumbs[i].addEventListener("mouseenter",function(){
                this.style.zIndex="2";
                this.style.transform = `scale(${scaleAmount},${scaleAmount})`;
                this.classList.add('z-depth-3');
            })
            imageThumbs[i].addEventListener("mouseout",function(){
                this.style.zIndex="1";
                this.style.transform = `scale(${resetAmount},${resetAmount})`;
                this.classList.remove('z-depth-3');

            })
    }
};

myEvents(imageThumbs);


// Lightbox js

openModalImg.forEach(function(element, index) {
    element.firstElementChild.id = parseInt(index) + 1;
});
thumbnailControlsImages.forEach(function(element, index) {
    element.id = parseInt(index) + 1;
});

showSlides(1);
function showSlides(n) {
    // console.log(slideIndex);
    // console.log(n);
    var i;
    var dots = thumbnailControlsImages;
    var slides = mySlides;
    // console.log(slides);

    if (n > slides.length) { slideIndex = 1 };
    if (n < 1) { slideIndex = slides.length };
    for ( i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i=0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace("active","");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active" ;
}
function currentSlide(n) {
    openModal();
    slideIndex = n
    showSlides(slideIndex);
}
function plusSlides(n) {
    showSlides (slideIndex += n);
}

function openModal () {
    lightboxModal.style.display = "block";
    navBar.style.display = 'none';
}
function closeModal() {
    lightboxModal.style.display="none";
    if (windowWidth >= 1100) {
        navBar.style.display = 'inherit';
    }
}

closeBtn.addEventListener('click',closeModal);

