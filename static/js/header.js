window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("navbar").style.top = "0";
    document.querySelector("#bill-logo").style.display = "none"
    document.querySelector("#body-main_nav").style.display = "none"
  } else {
    document.getElementById("navbar").style.top = "-90px";
    document.querySelector("#bill-logo").style.display = "block"
    document.querySelector("#body-main_nav").style.display = "block"
  }
}