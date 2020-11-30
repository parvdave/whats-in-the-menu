var counter = 1;

function changeDiv(i) {
  counter++;
  var firstSlide = document.getElementById("oneSlide");
  var secondSlide = document.getElementById("twoSlide");
  var thirdSlide = document.getElementById("threeSlide");

  if(i == 1) {
    counter = 1;
  }
  else if (i == 2) {
    counter = 2;
  }
  else if (i == 3){
    counter = 3;
  }

  var firstDIV = document.getElementById("oneDIV");
  var secondDIV = document.getElementById("twoDIV");
  var thirdDIV = document.getElementById("threeDIV");

  if (counter == 1) {
    firstDIV.classList.remove("hidden");
    secondDIV.classList.add("hidden");
    thirdDIV.classList.add("hidden");

    firstSlide.classList.add("active");
    secondSlide.classList.remove("active");
    thirdSlide.classList.remove("active");
  }

  if(counter == 2) {
    secondDIV.classList.remove("hidden");
    firstDIV.classList.add("hidden");
    thirdDIV.classList.add("hidden");

    firstSlide.classList.remove("active");
    secondSlide.classList.add("active");
    thirdSlide.classList.remove("active");
  }

  if(counter == 3) {
    thirdDIV.classList.remove("hidden");
    secondDIV.classList.add("hidden");
    firstDIV.classList.add("hidden");

    secondSlide.classList.remove("active");
    firstSlide.classList.remove("active");
    thirdSlide.classList.add("active");
  }

  if(counter == 4) {
    window.location.href = "./menu.html";
  }
}