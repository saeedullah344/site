burger = document.querySelector("burger");
navbarId = document.querySelector("background");
navbar = document.querySelector("nav_bar");

burger.addEventListener("click", () => {
  navbarId.classList.toggel("h_height");
  navbar.classList.toggel("v_class");
});
let count = document.getElementById('count_el')
console.log(count)
let count1 =0
function increment() {
  count1 = count1 +1
  count.innerText=count1
}

