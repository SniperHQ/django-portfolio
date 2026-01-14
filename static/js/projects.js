const carousel = document.querySelector('.carousel-3d');
const cards = Array.from(document.querySelectorAll('.carousel-card-link'));
const total = cards.length;
const radius = 300;
let rotationY = 0;

function updateCards() {
    const angleStep = 360 / total;
    cards.forEach((card, i) => {
        const angle = i * angleStep + rotationY;
        const rad = angle * Math.PI / 180;
        const x = Math.sin(rad) * radius;
        const z = Math.cos(rad) * radius;
        const scale = (z + radius) / (2 * radius) * 0.6 + 0.4;
        const opacity = (z + radius) / (2 * radius) * 0.5 + 0.5;
        card.style.transform = `translateX(${x}px) translateZ(${z}px) scale(${scale})`;
        card.style.zIndex = Math.floor(scale * 100);
        card.style.opacity = opacity;
    });
}
updateCards();

let autoRotateSpeed = 0.2;
function animate() {
    rotationY -= autoRotateSpeed;
    updateCards();
    requestAnimationFrame(animate);
}
animate();

let isDragging = false;
let startX;

function startDrag(e) {
    isDragging = true;
    startX = e.type.includes('touch') ? e.touches[0].clientX : e.clientX;
}

function onDrag(e) {
    if (!isDragging) return;
    const x = e.type.includes('touch') ? e.touches[0].clientX : e.clientX;
    const delta = x - startX;
    rotationY += delta * 0.3;
    startX = x;
    updateCards();
}

function endDrag() { isDragging = false; }

carousel.addEventListener('mousedown', startDrag);
carousel.addEventListener('mousemove', onDrag);
carousel.addEventListener('mouseup', endDrag);
carousel.addEventListener('mouseleave', endDrag);
carousel.addEventListener('touchstart', startDrag);
carousel.addEventListener('touchmove', onDrag);
carousel.addEventListener('touchend', endDrag);
