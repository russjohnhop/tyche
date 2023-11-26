document.addEventListener("DOMContentLoaded", function () {
  const mobileNavToggle = document.querySelector(".mobile-nav-toggle");
  const navList = document.querySelector(".nav-list");

  mobileNavToggle.addEventListener("click", function () {
    navList.classList.toggle("active");
  });
});
