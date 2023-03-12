function previewImage(event) {
  const preview = document.getElementById('id_card_preview');
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.onloadend = () => {
    preview.src = reader.result;
  };
  if (file) {
    reader.readAsDataURL(file);
  } else {
    preview.src = "";
  }
}

  