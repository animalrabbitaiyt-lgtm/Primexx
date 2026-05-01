// Header ELLEMENT

document.addEventListener('DOMContentLoaded', () => {



    // 1. Navigation Scroll Effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 2. Intersection Observer for Scroll Animations
    const revealElements = document.querySelectorAll('.reveal');

    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealOnScroll = new IntersectionObserver(function (entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });



    // Handle immediate active state for hero elements if already in view
    setTimeout(() => {
        document.querySelectorAll('.hero .reveal').forEach(el => {
            el.classList.add('active');
        });
    }, 100);

    // 4. Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navControls = document.querySelector('.nav-controls');

    if (menuToggle && navControls) {
        menuToggle.addEventListener('click', () => {
            navControls.classList.toggle('active');
        });
    }

    // 5. Modals Logic
    window.openModal = function (modalId) {
        const modal = document.getElementById(modalId);
        const overlay = document.getElementById('modal-overlay');
        if (modal && overlay) {
            modal.classList.add('active');
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden'; // prevent background scrolling
        }
    };

    window.closeModals = function () {
        document.querySelectorAll('.modal.active').forEach(modal => {
            modal.classList.remove('active');
        });
        const overlay = document.getElementById('modal-overlay');
        if (overlay) {
            overlay.classList.remove('active');
        }
        document.body.style.overflow = '';
    };

    // Close on overlay click
    const overlay = document.getElementById('modal-overlay');
    if (overlay) {
        overlay.addEventListener('click', closeModals);
    }

    // Close on button click
    document.querySelectorAll('.modal-close').forEach(btn => {
        btn.addEventListener('click', closeModals);
    });

    // 6. FAQ Accordion Logic
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const faqItem = question.parentElement;
            const faqAnswer = question.nextElementSibling;
            const isOpen = faqItem.classList.contains('active');

            // Close all items
            document.querySelectorAll('.faq-item').forEach(item => {
                item.classList.remove('active');
                item.querySelector('.faq-answer').style.maxHeight = null;
            });

            // Open clicked item if it wasn't open
            if (!isOpen) {
                faqItem.classList.add('active');
                faqAnswer.style.maxHeight = faqAnswer.scrollHeight + "px";
            }
        });
    });

    // 7. Multi-step Form Logic
    const formSteps = document.querySelectorAll('.form-step');
    const nextBtns = document.querySelectorAll('.next-btn');
    const prevBtns = document.querySelectorAll('.prev-btn');
    const progressBar = document.getElementById('progress-bar');
    const stepDisplay = document.getElementById('current-step-display');
    let currentStepNum = 0;
    let selectedService = '';

    const qualifierData = {
        "Video Editing & Content Creation": {
            step2: {
                title: "What type of videos do you need most?",
                name: "entry.155814216",
                options: ["Short form (TikTok/Reels)", "Long form (YouTube)", "Podcast Edits", "Vlog / Documentary"],
                gridClass: "vertical"
            },
            step3: {
                title: "What is your per-video editing budget?",
                name: "entry.1961719571",
                options: ["Under $100 / video", "$100 - $250 / video", "$250 - $500 / video", "$500+ / video"],
                gridClass: ""
            }
        },
        "Social Media Growth": {
            step2: {
                title: "What is your biggest social media bottleneck?",
                name: "entry.155814216",
                options: ["Inconsistent posting", "Low engagement / No reach", "Don't know what to post", "Need more qualified leads"],
                gridClass: "vertical"
            },
            step3: {
                title: "What is your monthly marketing budget?",
                name: "entry.1961719571",
                options: ["Under $1k / month", "$1k - $3k / month", "$3k - $5k / month", "$5k+ / month"],
                gridClass: ""
            }
        },
        "Website Development": {
            step2: {
                title: "What is the primary goal of the new website?",
                name: "entry.155814216",
                options: ["Generate more local leads", "Sell products (E-commerce)", "Brand credibility / Portfolio", "Custom Web App"],
                gridClass: "vertical"
            },
            step3: {
                title: "What is your website project budget?",
                name: "entry.1961719571",
                options: ["Under $3k", "$3k - $5k", "$5k - $10k", "$10k+"],
                gridClass: ""
            }
        },
        "Full Growth Retainer": {
            step2: {
                title: "What is your current monthly revenue?",
                name: "entry.155814216",
                options: ["Less than $10k / month", "$10k - $50k / month", "$50k - $100k / month", "$100k+ / month"],
                gridClass: "vertical"
            },
            step3: {
                title: "What is your monthly growth budget?",
                name: "entry.1961719571",
                options: ["Under $3k", "$3k - $5k", "$5k - $10k", "$10k+"],
                gridClass: ""
            }
        }
    };

    function populateDynamicSteps(service) {
        if (!qualifierData[service]) return;

        const data = qualifierData[service];

        // Populate Step 2
        const s2Title = document.getElementById('dynamic-step2-title');
        const s2Container = document.getElementById('dynamic-step2-options');
        if (s2Title && s2Container) {
            s2Title.innerText = data.step2.title;
            s2Container.className = `radio-grid ${data.step2.gridClass}`;
            s2Container.innerHTML = data.step2.options.map(opt => `
                <label class="radio-card">
                    <input type="radio" name="${data.step2.name}" value="${opt}" required>
                    <span>${opt}</span>
                </label>
            `).join('');
        }

        // Populate Step 3
        const s3Title = document.getElementById('dynamic-step3-title');
        const s3Container = document.getElementById('dynamic-step3-options');
        if (s3Title && s3Container) {
            s3Title.innerText = data.step3.title;
            s3Container.className = `radio-grid ${data.step3.gridClass}`;
            s3Container.innerHTML = data.step3.options.map(opt => `
                <label class="radio-card">
                    <input type="radio" name="${data.step3.name}" value="${opt}" required>
                    <span>${opt}</span>
                </label>
            `).join('');
        }
    }

    function updateFormSteps() {
        formSteps.forEach((step, index) => {
            step.classList.toggle('active', index === currentStepNum);
        });

        if (progressBar && stepDisplay) {
            const progressPercentage = ((currentStepNum + 1) / formSteps.length) * 100;
            progressBar.style.width = progressPercentage + '%';
            stepDisplay.innerText = currentStepNum + 1;
        }
    }

    nextBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (formSteps.length > 0) {
                const currentStepEl = formSteps[currentStepNum];
                const radios = currentStepEl.querySelectorAll('input[type="radio"]');

                let isValid = true;
                if (radios.length > 0) {
                    isValid = Array.from(radios).some(radio => radio.checked);
                    if (!isValid) {
                        alert('Please select an option before continuing.');
                        return;
                    }

                    // If we are passing step 1, get choice and populate step 2 and 3
                    if (currentStepNum === 0) {
                        const selectedRadio = Array.from(radios).find(radio => radio.checked);
                        if (selectedRadio.value !== selectedService) {
                            selectedService = selectedRadio.value;
                            populateDynamicSteps(selectedService);
                        }
                    }
                }

                if (currentStepNum < formSteps.length - 1) {
                    currentStepNum++;
                    updateFormSteps();
                }
            }
        });
    });

    prevBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentStepNum > 0) {
                currentStepNum--;
                updateFormSteps();
            }
        });
    });

});
