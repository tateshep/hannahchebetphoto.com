/*
    Animate forward arrow for blog cards
*/
HTMLCollection.prototype.forEach = Array.prototype.forEach;
var collectionTitle = document.getElementsByClassName('collection-title-animation');
var blogCard = document.getElementsByClassName('card');

function animateArrow() {
    console.log('start');
    console.log(this.querySelector('.collection-title-animation'));
    let forwardArrows = this.querySelector('.collection-title-animation');
    forwardArrows.firstElementChild.classList.add('arrow-animation');
}
function stopAnimate() {
    console.log('stop');
    let forwardArrows = this.querySelector('.collection-title-animation');

    forwardArrows.firstElementChild.classList.remove('arrow-animation');
}

blogCard.forEach(function(e){
    e.addEventListener('mouseenter',animateArrow);
    e.addEventListener('mouseleave', stopAnimate);
})