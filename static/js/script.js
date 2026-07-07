// ===========================================
// OptiCrop Professional JavaScript
// ===========================================

// Navbar Background Change on Scroll
window.addEventListener("scroll", function () {

    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 50) {

        navbar.classList.add("shadow-lg");

    } else {

        navbar.classList.remove("shadow-lg");

    }

});

// ===========================================
// Smooth Scroll
// ===========================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        document.querySelector(this.getAttribute("href")).scrollIntoView({

            behavior: "smooth"

        });

    });

});

// ===========================================
// Counter Animation
// ===========================================

const counters = document.querySelectorAll(".stat-card h2");

const speed = 150;

const animateCounter = (counter) => {

    const target = parseFloat(counter.innerText);

    if (isNaN(target)) return;

    let count = 0;

    const update = () => {

        const increment = target / speed;

        if (count < target) {

            count += increment;

            if (counter.innerText.includes("%")) {

                counter.innerText = count.toFixed(1) + "%";

            } else if (counter.innerText.includes("+")) {

                counter.innerText = Math.floor(count) + "+";

            } else {

                counter.innerText = Math.floor(count);

            }

            requestAnimationFrame(update);

        } else {

            counter.innerText = counter.dataset.original;

        }

    };

    update();

};

window.addEventListener("load", () => {

    counters.forEach(counter => {

        counter.dataset.original = counter.innerText;

        animateCounter(counter);

    });

});

// ===========================================
// Loading Spinner on Prediction Form
// ===========================================

const predictionForm = document.querySelector("form");

if (predictionForm) {

    predictionForm.addEventListener("submit", function () {

        const button = this.querySelector("button");

        button.disabled = true;

        button.innerHTML =

            `<span class="spinner-border spinner-border-sm"></span>

            Predicting...`;

    });

}

// ===========================================
// Fade Animation
// ===========================================

const cards = document.querySelectorAll(

".feature-card,.stat-card,.work-card,.info-box,.objective-card"

);

const observer = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.classList.add("show");

        }

    });

}, {

    threshold: .2

});

cards.forEach(card => {

    card.classList.add("hidden");

    observer.observe(card);

});

// ===========================================
// Back To Top Button
// ===========================================

const topBtn = document.createElement("button");

topBtn.innerHTML =

'<i class="fa-solid fa-arrow-up"></i>';

topBtn.className = "top-button";

document.body.appendChild(topBtn);

window.addEventListener("scroll", () => {

    if (window.scrollY > 300) {

        topBtn.style.display = "block";

    } else {

        topBtn.style.display = "none";

    }

});

topBtn.onclick = () => {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

};

// ===========================================
// Input Validation
// ===========================================

const inputs = document.querySelectorAll("input[type='number']");

inputs.forEach(input => {

    input.addEventListener("input", () => {

        if (parseFloat(input.value) < 0) {

            input.value = "";

        }

    });

});