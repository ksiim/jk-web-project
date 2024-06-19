function previewAvatar(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function() {
      const imgElement = document.getElementById('avatarPreview');
      const placeholderElement = document.getElementById('avatarPlaceholder');
      if (imgElement) {
        imgElement.src = reader.result;
      } else if (placeholderElement) {
        placeholderElement.innerHTML = `<img src="${reader.result}" alt="Аватар" id="avatarPreview" class="img-fluid">`;
      }
    };
    reader.readAsDataURL(file);
  }

  document.addEventListener('DOMContentLoaded', function () {
    const bgOptions = document.querySelectorAll('.bg-option');
    const bgModalOptions = document.querySelectorAll('.bg-option-modal');
    const currentBgThumbnail = document.querySelector('.background-thumbnail');

    bgOptions.forEach(option => {
      option.addEventListener('click', function () {
        bgOptions.forEach(opt => opt.classList.remove('selected'));
        this.classList.add('selected');
        document.getElementById('id_profile_background').value = this.dataset.bg;
      });
    });

    bgModalOptions.forEach(option => {
      option.addEventListener('click', function () {
        bgModalOptions.forEach(opt => opt.classList.remove('selected'));
        this.classList.add('selected');
        document.getElementById('id_profile_background').value = this.dataset.bg;
        currentBgThumbnail.src = this.src;
        var myModalEl = document.getElementById('backgroundModal');
        var modal = bootstrap.Modal.getInstance(myModalEl);
        modal.hide();
      });
    });
  });