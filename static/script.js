// JavaScript function to update file name
function updateFileName() {
  var fileInput = document.getElementById('file-upload');
  var fileName = document.getElementById('file-name');
  fileName.textContent = fileInput.files[0].name; // Display selected file name
}
