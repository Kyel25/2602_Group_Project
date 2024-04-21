function toggleSettings() {
  var popup = document.getElementById("settings-popup");
  if (popup.style.display === "block") {
    popup.style.display = "none";
  } else {
    popup.style.display = "block";
  }
}





var slideIndex = 0;
var slides = document.querySelectorAll('.mySlides');
var dots = document.querySelectorAll('.dot');
var slideTimeout; // Declare slideTimeout variable

showSlides();

function showSlides() {
  // Set slideIndex to 0 to display the first slide
  slideIndex = 0;
  showSlide(slideIndex);
}

function showSlide(n) {
  var i;
  if (n >= slides.length) {slideIndex = 0}
  if (n < 0) {slideIndex = slides.length - 1}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex].style.display = "block";
  slides[slideIndex].style.opacity = 1; // Ensure opacity is set to 1 for the current slide
  // Automatically transition to the next slide after 5 seconds
  slideTimeout = setTimeout(function() {
    plusSlides(1);
  }, 5000); // Adjust the interval as needed (in milliseconds)
}

function currentSlide(n) {
  clearTimeout(slideTimeout);
  // Hide all slides
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.opacity = 0;
  }
  slideIndex = n;
  // Display the current slide
  slides[slideIndex].style.opacity = 1;
  showDot(slideIndex);
}

function plusSlides(n) {
  clearTimeout(slideTimeout);
  showSlide(slideIndex += n);
}

function showDot(n) {
  for (let i = 0; i < dots.length; i++) {
    dots[i].classList.remove("active");
  }
  dots[n].classList.add("active");
}

// Add event listeners to radio buttons
document.querySelectorAll('.slide-radio').forEach(function(radio, index) {
  radio.addEventListener('click', function() {
    currentSlide(index);
  });
});

// Start the automatic slideshow
showSlide(slideIndex);


