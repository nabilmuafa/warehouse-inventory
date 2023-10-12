window.addEventListener("DOMContentLoaded", (event) => {
  const userBtn = document.getElementById("user-dropdown");
  const dropdownContent = document.getElementById("dropdown-content");
  if (userBtn) {
    userBtn.addEventListener("click", function () {
      dropdownContent.classList.toggle("hidden");
    });
  }
  if (dropdownContent) {
    dropdownContent.addEventListener("click", function (event) {
      event.stopPropagation();
    });
  }
});
