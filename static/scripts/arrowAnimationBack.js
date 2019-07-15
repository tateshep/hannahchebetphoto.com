/*
    Animate back arrow
*/
HTMLCollection.prototype.forEach = Array.prototype.forEach;
var arrowBack = document.getElementsByClassName('arrow-back');
// var forwardArrows = document.getElementsByClassName('arrow-animation');

function animateArrow() {
    console.log('start');
    this.firstElementChild.classList.add('arrow-animation-back');
}
function stopAnimate() {
    console.log('stop');
    this.firstElementChild.classList.remove('arrow-animation-back');
}

arrowBack.forEach(function(e){
    e.addEventListener('mouseenter',animateArrow);
    e.addEventListener('mouseleave', stopAnimate);
})