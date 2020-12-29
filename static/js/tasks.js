const inputBox = document.querySelector(".input-field input");
const addBtn = document.querySelector(".input-field button");

inputBox.onkeyup = () => {
  // get user input
  let userData = inputBox.value;
  // check null input
  if (userData.trim() != 0) {
    addBtn.classList.add("active");
  } else {
    addBtn.classList.remove("active");
  }
};
