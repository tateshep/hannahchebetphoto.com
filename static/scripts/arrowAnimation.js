/*
    Animate forward arrow
*/
HTMLCollection.prototype.forEach = Array.prototype.forEach;
var collectionTitle = document.getElementsByClassName('collection-title-animation');
var forwardArrows = document.getElementsByClassName('arrow-animation');

function animateArrow() {
    console.log('start');
    this.firstElementChild.classList.add('arrow-animation');
}
function stopAnimate() {
    console.log('stop');
    this.firstElementChild.classList.remove('arrow-animation');
}

collectionTitle.forEach(function(e){
    e.addEventListener('mouseenter',animateArrow);
    e.addEventListener('mouseleave', stopAnimate);
})