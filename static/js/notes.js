handleSaveButtonActiveState = () => {
  const notesTitle = document.getElementById("title-input");
  const saveButton = document.getElementById("save-button");
  let userInput = notesTitle.value;

  if(userInput.trim() != 0) {
    saveButton.classList.add("active");
  } else {
    saveButton.classList.remove("active");
  }
}


togglePopup = () => {
  const addNoteButton = document.getElementById("add-note-button");
  addNoteButton.classList.toggle("active");
}