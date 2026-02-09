// Auto-hide messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => message.remove(), 300);
        }, 5000);
    });
    
    // Mobile menu toggle
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileToggle && navLinks) {
        mobileToggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            this.querySelector('i').classList.toggle('fa-bars');
            this.querySelector('i').classList.toggle('fa-times');
        });
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Category filtering
document.addEventListener("DOMContentLoaded", function () {
    const categoryTags = document.querySelectorAll(".category-tag");
    const products = document.querySelectorAll(".product-card");

    // Only run on home page
    if (window.location.pathname === '/' || window.location.pathname === '/home/') {
        categoryTags.forEach(tag => {
            tag.addEventListener("click", function (e) {
                // If it's a link to category page, let it navigate
                if (this.href && this.href.includes('/category/')) {
                    return; // Let the link work normally
                }
                
                e.preventDefault();

                // Update active state
                categoryTags.forEach(t => t.classList.remove("active"));
                this.classList.add("active");

                const selectedCategory = this.textContent.trim().toLowerCase();

                // Filter products
                products.forEach(product => {
                    const productCategory = product.dataset.category;
                    
                    if (selectedCategory === "all" || productCategory === selectedCategory) {
                        product.style.display = "block";
                        product.style.animation = "fadeIn 0.3s ease";
                    } else {
                        product.style.display = "none";
                    }
                });
            });
        });
    }
});

// Search functionality enhancement
const searchInput = document.getElementById('searchInput');
if (searchInput) {
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            this.closest('form').submit();
        }
    });
}

// Add to cart animation
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function(e) {
        // Create a flying cart icon animation
        const icon = document.createElement('i');
        icon.className = 'fas fa-shopping-cart';
        icon.style.position = 'fixed';
        icon.style.left = e.clientX + 'px';
        icon.style.top = e.clientY + 'px';
        icon.style.fontSize = '24px';
        icon.style.color = '#6366f1';
        icon.style.zIndex = '9999';
        icon.style.pointerEvents = 'none';
        icon.style.animation = 'flyToCart 0.8s ease-out';
        
        document.body.appendChild(icon);
        
        setTimeout(() => icon.remove(), 800);
    });
});

// Intersection Observer for scroll animations
const revealItems = document.querySelectorAll(
    ".product-card, .value-card, .timeline-item, .team-card"
);

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = 1;
            entry.target.style.transform = "translateY(0)";
        }
    });
}, { threshold: 0.15 });

revealItems.forEach(item => {
    item.style.opacity = 0;
    item.style.transform = "translateY(20px)";
    item.style.transition = "opacity 0.5s ease, transform 0.5s ease";
    observer.observe(item);
});

// Newsletter form handling
const newsletterForm = document.querySelector('.newsletter-form');
if (newsletterForm) {
    newsletterForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const email = this.querySelector('input[type="email"]').value;
        
        // Show success message
        const message = document.createElement('div');
        message.className = 'alert alert-success';
        message.innerHTML = '<i class="fas fa-check-circle"></i> Thank you for subscribing!';
        message.style.position = 'fixed';
        message.style.top = '80px';
        message.style.right = '20px';
        message.style.zIndex = '9999';
        
        document.body.appendChild(message);
        
        setTimeout(() => message.remove(), 3000);
        
        this.reset();
    });
}

// Image lazy loading fallback
document.querySelectorAll('img[loading="lazy"]').forEach(img => {
    img.addEventListener('error', function() {
        this.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="200" height="200"%3E%3Crect fill="%23f0f0f0" width="200" height="200"/%3E%3Ctext fill="%23999" x="50%25" y="50%25" text-anchor="middle" dy=".3em"%3ENo Image%3C/text%3E%3C/svg%3E';
    });
});

// Cart count update animation
function updateCartCount() {
    const cartCount = document.querySelector('.cart-count');
    if (cartCount) {
        cartCount.style.animation = 'pulse 0.3s ease';
        setTimeout(() => {
            cartCount.style.animation = '';
        }, 300);
    }
}

// Confirm before removing items
document.querySelectorAll('a[href*="remove"]').forEach(link => {
    if (!link.hasAttribute('onclick')) {
        link.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to remove this item?')) {
                e.preventDefault();
            }
        });
    }
});

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: scale(0.9);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    @keyframes flyToCart {
        0% {
            transform: translate(0, 0) scale(1);
            opacity: 1;
        }
        100% {
            transform: translate(calc(100vw - 200px), -100px) scale(0.3);
            opacity: 0;
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.2);
        }
    }
`;
document.head.appendChild(style);

// Back to top button
const backToTop = document.createElement('button');
backToTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
backToTop.className = 'back-to-top';
backToTop.style.cssText = `
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: var(--primary);
    color: white;
    border: none;
    cursor: pointer;
    display: none;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    z-index: 1000;
    transition: all 0.3s;
`;

document.body.appendChild(backToTop);

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTop.style.display = 'flex';
    } else {
        backToTop.style.display = 'none';
    }
});

backToTop.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

backToTop.addEventListener('mouseenter', function() {
    this.style.transform = 'translateY(-5px)';
});

backToTop.addEventListener('mouseleave', function() {
    this.style.transform = 'translateY(0)';
});

console.log('🛒 ShopEasy loaded successfully!');
