/*
    Animate forward arrow
*/
HTMLCollection.prototype.forEach = Array.prototype.forEach;
var cardImage = document.getElementsByClassName('card-image');
var cardTitle = document.querySelector('.card-title');
console.log(cardTitle);
// var downwardArrows = document.getElementsByClassName('arrow-animation');

function animateArrow() {
    console.log('start');
    cardTitle.classList.add('arrow-animation-vertical');
}
function stopAnimate() {
    console.log('stop');
    cardTitle.classList.remove('arrow-animation-vertical');
}

cardImage.forEach(function(e){
    e.addEventListener('mouseenter',animateArrow);
    e.addEventListener('mouseleave', stopAnimate);
})