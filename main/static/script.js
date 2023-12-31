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
document.getElementById("confirm-modal").addEventListener("click", closeModal);
document.getElementById("cancel-modal").addEventListener("click", closeModal);
document.getElementById("modal-panel").addEventListener("click", closeModal);

function addItems() {
  fetch("create-ajax/", {
    method: "POST",
    body: new FormData(document.querySelector("#form")),
  }).then(refreshProducts);

  document.getElementById("form").reset();
  return false;
}

async function getItems() {
  return fetch("user-json/").then((res) => res.json());
}

async function deleteItems(id) {
  let form = new FormData();
  form.append("id", id);
  await fetch("delete/", {
    method: "POST",
    body: form,
  }).then(refreshProducts);
}

async function increment(id) {
  let form = new FormData();
  form.append("id", id);
  await fetch("inc/", {
    method: "POST",
    body: form,
  });
  refreshProducts();
}

async function decrement(id) {
  let form = new FormData();
  form.append("id", id);
  await fetch("dec/", {
    method: "POST",
    body: form,
  });
  refreshProducts();
}

async function refreshProducts() {
  let items = await getItems();
  let htmlString = ``;
  items.forEach((el) => {
    htmlString += `\n<div class="h-72 md:h-80 bg-white border-2 border-gray-200 rounded-lg p-6">
      <div class="flex flex-wrap justify-between items-center md:pb-4 pb-3">
          <p class="text-xl md:text-2xl font-bold">${el.fields.name}</p>
          <div class="flex font text-sm md:text-base items-center text-lg md:gap-6 gap-4">
              <div class="flex amount-modifier rounded-lg border-2 items-center gap-4 md:px-2 px-1 py-1">
                  <button ${
                    el.fields.amount == 1 ? "disabled " : ""
                  }class="dec-btn rounded-full text-blue-500 disabled:text-gray-500 transition-color ease-in-out duration-100 md:hover:bg-white hover:bg-gray-300 disabled:md:hover:text-gray-500 md:hover:text-blue-500" onclick="decrement(${
      el.pk
    })">
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M18 12H6" />
                      </svg>                                          
                  </button>
                  <p id="amount-field-${el.pk}" class="amt pt-0.5 md:pt-0">${
      el.fields.amount
    }</p>
                  <button class="rounded-full text-blue-500 transition-color ease-in-out duration-100 md:hover:bg-white hover:bg-gray-300 md:hover:text-blue-500" onclick="increment(${
                    el.pk
                  })">
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m6-6H6" />
                      </svg>                                                  
                  </button>
              </div>
              <button class="transition-color ease-in-out duration-100 hover:text-red-500" onclick="deleteItems(${
                el.pk
              })">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                  </svg>                      
              </button>
          </div>
      </div>
      <p class="text-sm md:text-base">${el.fields.description}</p>
  </div>`;
  });

  document.getElementById("items-display").innerHTML = htmlString;
}

refreshProducts();
