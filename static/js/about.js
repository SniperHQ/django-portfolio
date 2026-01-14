document.addEventListener("DOMContentLoaded", () => {
    const skillCircles = document.querySelectorAll(".skill-circle");

    if (!skillCircles.length) return;

    skillCircles.forEach(circle => {
        const progress = circle.querySelector(".skill-progress");
        const radius = progress.r.baseVal.value;
        const circumference = 2 * Math.PI * radius;
        progress.style.strokeDasharray = circumference;
        progress.style.strokeDashoffset = circumference;
    });

    function getColor(percent) {
        if (percent < 50) return "#e74c3c";
        if (percent < 80) return "#f39c12";
        return "#2ecc71";
    }

    function animateSkills() {
        skillCircles.forEach(circle => {
            const rect = circle.getBoundingClientRect();
            if (rect.top < window.innerHeight - 80 && !circle.classList.contains("active")) {
                circle.classList.add("active");

                const percent = parseInt(circle.dataset.percentage);
                const progress = circle.querySelector(".skill-progress");
                const number = circle.querySelector(".skill-percentage");
                const radius = progress.r.baseVal.value;
                const circumference = 2 * Math.PI * radius;

                progress.style.stroke = getColor(percent);

                let start = performance.now();
                const duration = 1500;

                function animate(now) {
                    const elapsed = now - start;
                    const t = Math.min(elapsed / duration, 1);
                    const current = Math.floor(t * percent);

                    progress.style.strokeDashoffset =
                        circumference - (current / 100) * circumference;
                    number.textContent = current + "%";

                    if (t < 1) requestAnimationFrame(animate);
                }

                requestAnimationFrame(animate);
            }
        });
    }

    window.addEventListener("scroll", animateSkills);
    animateSkills();
});
