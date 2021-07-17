let image = document.querySelectorAll('.member-image');
const abouts = document.querySelectorAll(".member-about");

// console.log(image)
// console.log(abouts)

image.forEach(btn => {
  btn.addEventListener("click", showAbout)
});


function showAbout(e) {
  this.nextElementSibling.classList.toggle("show")
};

// abouts.forEach(about => about.nextElementSibling.classList.toggle("show"));
// console.log('working');

