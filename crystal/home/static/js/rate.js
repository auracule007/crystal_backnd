// rating
// const stars = document.querySelectorAll(".star");
// const selectedRating = document.getElementById("selected-rating");

// stars.forEach((star) => {
//   star.addEventListener("click", () => {
//     const rating = parseInt(star.getAttribute("data-value"));

//     // Change star colors for the rated stars
//     stars.forEach((s, index) => {
//       if (index < rating) {
//         s.classList.add("rated");
//       } else {
//         s.classList.remove("rated");
//       }
//     });

//     selectedRating.textContent = rating;
//   });
// });

const stars = document.querySelectorAll(".star");
const selectedRating = document.getElementById("selected-rating");
const localStorageKey = "productRating";

// Check if there is a saved rating in localStorage
const savedRating = localStorage.getItem(localStorageKey);

if (savedRating) {
  // Display the saved rating
  selectedRating.textContent = savedRating;

  // Mark stars up to the saved rating
  stars.forEach((star, index) => {
    if (index < savedRating) {
      star.classList.add("rated");
    }
  });
}

stars.forEach((star) => {
  star.addEventListener("click", () => {
    const rating = parseInt(star.getAttribute("data-value"));

    // Change star colors for the rated stars
    stars.forEach((s, index) => {
      if (index < rating) {
        s.classList.add("rated");
      } else {
        s.classList.remove("rated");
      }
    });

    selectedRating.textContent = rating;

    // Save the rating to localStorage
    localStorage.setItem(localStorageKey, rating);
  });
});
