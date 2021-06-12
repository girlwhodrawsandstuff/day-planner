const wrapper = document.querySelector(".wrapper");
      const defaultBtn = document.querySelector("#default-btn");
      const customBtn = document.querySelector("#custom-btn");
      const img = document.querySelector("img");
      let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;
      function defaultBtnActive() {
        defaultBtn.click();
      }
      defaultBtn.addEventListener("change", function() {
        const file = this.files[0];
        if(file) {
          const reader = new FileReader();
          reader.onload = function() {
            const result = reader.result;
            img.src = result;
            wrapper.classList.add("active");
          }
          reader.readAsDataURL(file);
        }
      });