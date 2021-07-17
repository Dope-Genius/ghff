let buttton = document.querySelectorAll('.menu');
const body = document.querySelector(".body");
const links = document.querySelector("#navlinks");

buttton.forEach(btn => {
  btn.addEventListener("click", myFunction)
});


function myFunction() {
  body.classList.toggle("active");
  links.classList.toggle("active");
  console.log('working');
}