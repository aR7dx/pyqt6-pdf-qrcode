const cursorOutline = document.querySelector("[data-cursor-outline]");

window.addEventListener('mousemove', function (e) {

  const posX = e.clientX;
  const posY = e.clientY;

  cursorOutline.style.left = `${posX}px`;
  cursorOutline.style.top = `${posY}px`;

  cursorOutline.animate({
    left: `${posX}px`,
    top: `${posY}px`
  }, { duration: 500, fill: 'forwards' });
});