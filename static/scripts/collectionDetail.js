// Scaling image animation js


let imageThumbs = document.getElementsByClassName('collection-detail-image');
let myModal = document.getElementById('myModal');
let imageThumbsArray= [];
let scaleAmount = 1.30;
let resetAmount = 1;

function myEvents (imageThumbs) {
        for (i=0;i<imageThumbs.length;i++) {
            imageThumbs[i].addEventListener("click", openModal );
            imageThumbs[i].addEventListener("mouseenter",function(){
                this.parentElement.style.zIndex="2";
                this.style.transform = `scale(${scaleAmount},${scaleAmount})`;
                // console.log(' scale');
            })
            imageThumbs[i].addEventListener("mouseout",function(){
                this.parentElement.style.zIndex="1";
                this.style.transform = `scale(${resetAmount},${resetAmount})`;
                // console.log(' unscale');
            })
    }
};


function openModal () {
    console.log("clicked");
    myModal.style.display = "block";

}

myEvents(imageThumbs);

