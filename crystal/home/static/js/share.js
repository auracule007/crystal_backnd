document.addEventListener("DOMContentLoaded", function () {
  // WhatsApp sharing function
  function shareOnWhatsApp() {
    const productLink = "http://127.0.0.1:8000/product_details/id/"; // Replace with your actual product link
    // const productLink = "https://example.com/your-product-link"; 
    const encodedLink = encodeURIComponent(productLink);
    const whatsappShareLink = `https://api.whatsapp.com/send?text=${encodedLink}`;

    window.open(whatsappShareLink);
  }
  // http://127.0.0.1:8000/product_details/2/

  // Twitter sharing function
  function shareOnTwitter() {
    const productLink = "http://127.0.0.1:8000/product_details/id/"; // Replace with your actual product link
    const encodedLink = encodeURIComponent(productLink);
    const twitterShareLink = `https://twitter.com/intent/tweet?url=${encodedLink}`;

    window.open(twitterShareLink);
  }

  const whatsappButton = document.getElementById("whatsapp-button");
  const twitterButton = document.getElementById("twitter-button");

  whatsappButton.addEventListener("click", shareOnWhatsApp);
  twitterButton.addEventListener("click", shareOnTwitter);
});
