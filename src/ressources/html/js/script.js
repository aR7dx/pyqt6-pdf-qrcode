// Le module 'qrcode.js' est utilisé pour faire la génération de qrcode.
// La page github de 'qrcode.js' => 'https://github.com/davidshimjs/qrcodejs'.


// QRCODE PANEL

document.addEventListener('DOMContentLoaded', (event) => {
  const generateQRLink = document.getElementById('generateQRLink'); // genere le qrcode en fonction de l'input générer
  const saveQRCodeLink  = document.getElementById('saveQrLink'); // propose d'enregistrer le qrcode 
  const removeInputLink = document.getElementById('removeInputLink'); // efface la valeur inscrite dans l'input
  const fileSelectorLink  = document.getElementById('fileSelectorLink'); // bouton importation de fichier
  const hiddenFileInput = document.getElementById('hiddenFileInput');
  // const openPdfFolderLink = document.getElementById('openPdfFolderLink'); // ouvre le dossier des pdf
  // const hiddenFolderInput = document.getElementById('hiddenFolderInput');
  const fileNameDisplayInput = document.getElementById('fileNameDisplayInput'); // Visible Input Field
  const qrCodeContainer = document.getElementById('qrcode');


  // reset input to prevent remnants of previous generations
  resetInput();


  // generate qrcode button
  fileNameDisplayInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
      generateQRCode();
    }
  });

  generateQRLink.addEventListener('click', (e) => {
    generateQRCode();
  });

  function generateQRCode() {
    const value = fileNameDisplayInput.value;
    if (value.trim() !== '') {
        qrCodeContainer.innerHTML = ''; // Efface le précédent QR code

        try {
          new QRCode(qrCodeContainer, value); // Genere un nouveau QR code

          saveQRCodeLink .classList.remove('disabled');
          removeInputLink.classList.remove('disabled');
          
        } catch {
          alert('Veuillez télécharger le fichier qrcode.js pour générer des qrcodes :\nhttps://github.com/davidshimjs/qrcodejs\n\nUne fois ce fichier téléchargé, placer-le dans le répertoire : ./src/ressources/html/js/');
        }
    } else {
      alert('Veuillez entrer une valeur afin de pouvoir générer un qrcode.');
    }
  }



  // save qrcode button
  saveQRCodeLink.addEventListener('click', function(event) {
    event.preventDefault();

    const qrCodeDataURL = qrCodeContainer.querySelector('img').src;

    fetch(qrCodeDataURL)
      .then(response => response.blob())
      .then(blob => {

        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);

        link.download = 'qrcode.png';

        link.click();

        URL.revokeObjectURL(link.href);

    });
  });



  // remove qrcode button
  removeInputLink.addEventListener('click', function(event) {
    event.preventDefault();
    if (removeInputLink.classList.contains('disabled')) {
      //pass
    } else {
      resetInput();
    }

    qrCodeContainer.innerHTML = '';

    saveQRCodeLink .classList.add('disabled');
    removeInputLink.classList.add('disabled');
  });

  function resetInput() {
    fileNameDisplayInput.value = '';
    hiddenFileInput.value = '';
    fileNameDisplayInput.classList.remove('disabled');
    fileNameDisplayInput.removeEventListener('focus', preventFocus);
  }



  // generate from file button
  fileSelectorLink.addEventListener('click', (e) => {
    e.preventDefault(); // Prevent the link from navigating.
    hiddenFileInput.click(); // Trigger file selection dialog.
  });

  hiddenFileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];

    if (file) {
      resetInput();
      fileNameDisplayInput.value = file.name;
      fileNameDisplayInput.classList.add('disabled');
      fileNameDisplayInput.addEventListener('focus', preventFocus);
    }
  });

  function preventFocus() {
    this.blur(); // Blur the input field immediately, preventing further interaction
  }

});
