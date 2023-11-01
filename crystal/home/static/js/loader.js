const container = document.querySelector(".kevin");

window.addEventListener("load", () => {
  container.style.display = "none";
});

const profileButton = document.getElementById("profile");
const ordersButton = document.getElementById("orders");
const reviewsButton = document.getElementById("reviews");
const profileContainer = document.getElementById("profile-container");
const ordersContainer = document.getElementById("orders-container");
const reviewsContainer = document.getElementById("reviews-container");

// Initially, show the profile container and hide the orders container
profileContainer.style.display = "block";
ordersContainer.style.display = "none";
reviewsContainer.style.display = "none";

profileButton.addEventListener("click", () => {
  // Show the profile container and hide the orders container
  profileContainer.style.display = "block";
  ordersContainer.style.display = "none";
  reviewsContainer.style.display = "none";
});

ordersButton.addEventListener("click", () => {
  // Show the orders container and hide the profile container
  ordersContainer.style.display = "block";
  profileContainer.style.display = "none";
  reviewsContainer.style.display = "none";
});

reviewsButton.addEventListener("click", () => {
  // Show the reviews container and hide the orders container
  reviewsContainer.style.display = "block";
  ordersContainer.style.display = "none";
  profileContainer.style.display = "none";
});



// second item 
var Form1 = document.getElementById("Form1");
var Form2 = document.getElementById("Form2");
var Form3 = document.getElementById("Form3");

var Next1 = document.getElementById("next1");
var Next2 = document.getElementById("next2");
var Back1 = document.getElementById("back1");
var Back2 = document.getElementById("back2");

var progress = document.getElementById("progress2");

Next1.onclick = function(){
    Form1.style.left = "-500px";
    Form2.style.left = "40px";
    progress.style.width = "240px";
}

Back1.onclick = function(){
    Form1.style.left = "-20px";
    Form2.style.left = "500px";
    progress.style.width = "120px";
}

Next2.onclick = function(){
    Form2.style.left = "-500px";
    Form3.style.left = "40px";
    progress.style.width = "360px"; 
}

Back2.onclick = function(){
    Form2.style.left = "-40px";
    Form3.style.left = "500px";
    progress.style.width = "240px";
}