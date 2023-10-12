window.addEventListener("DOMContentLoaded", (event) => {
  const userBtn = document.getElementById("user-dropdown");
  const dropdownContent = document.getElementById("dropdown-content");
  const modal = document.getElementById("modal");

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

  function openModal() {
    modal.classList.remove("hidden");
  }

  function closeModal() {
    modal.classList.add("hidden");
  }

  document.getElementById("modal-button").addEventListener("click", openModal);
  document
    .getElementById("modal-button-mobile")
    .addEventListener("click", openModal);
  document.getElementById("confirm-modal").addEventListener("click", addItems);
  document
    .getElementById("confirm-modal")
    .addEventListener("click", closeModal);
  document.getElementById("cancel-modal").addEventListener("click", closeModal);
});
