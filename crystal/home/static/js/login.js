const loginBtn = document.getElementById("login");
const registerBtn = document.getElementById("register");
const loginContainer = document.getElementById("login-container");
const registerContainer = document.getElementById("register-container");

// Initially, show the profile container and hide the orders container
loginContainer.style.display = "block";
registerContainer.style.display = "none";

loginBtn.addEventListener("click", () => {
  // Show the profile container and hide the orders container
  loginContainer.style.display = "block";
  registerContainer.style.display = "none";
});

registerBtn.addEventListener("click", () => {
  // Show the orders container and hide the profile container
  registerContainer.style.display = "block";
  loginContainer.style.display = "none";
});



document.addEventListener("DOMContentLoaded", function() {
  const minusButton = document.querySelector(".minus");
  const plusButton = document.querySelector(".plus");
  const quantityElement = document.querySelector(".item-quantity");

  // Initialize item quantity
  let quantity = 1;

  // Function to update and display the item quantity
  function updateQuantity() {
      quantityElement.textContent = quantity;
  }

  // Event listener for the minus button
  minusButton.addEventListener("click", function() {
      if (quantity > 1) {
          quantity -= 1;
          updateQuantity();
      }
  });

  // Event listener for the plus button
  plusButton.addEventListener("click", function() {
      quantity += 1;
      updateQuantity();
  });
});

var Form1 = document.getElementById("form1");
var Form2 = document.getElementById("form2");
var Form3 = document.getElementById("form3");

var Next1 = document.getElementById("Next1");
var Next2 = document.getElementById("Next2");
var Back1 = document.getElementById("Back1");
var Back2 = document.getElementById("Back2");

var progress = document.getElementById("progress");

Next1.onclick = function(){
    Form1.style.left = "-1500px";
    Form2.style.left = "-20px";
    progress.style.width = "240px";
}

Back1.onclick = function(){
    Form1.style.left = "-20px";
    Form2.style.left = "1500px";
    progress.style.width = "120px";
}

Next2.onclick = function(){
    Form2.style.left = "-1500px";
    Form3.style.left = "20px";
    progress.style.width = "360px"; 
}

Back2.onclick = function(){
    Form2.style.left = "-25px";
    Form3.style.left = "1500px";
    progress.style.width = "240px";
}