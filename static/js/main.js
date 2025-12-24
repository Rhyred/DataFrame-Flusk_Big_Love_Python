// ===========================
// PROFESSIONAL DASHBOARD JS
// ===========================

// Dark Mode Management
class DarkMode {
    constructor() {
        this.html = document.documentElement;
        this.isDark = localStorage.getItem('darkMode') === 'true';
        this.init();
    }
    
    init() {
        // Check saved preference first
        if (this.isDark) {
            this.enable();
        } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            this.enable();
        }
        
        // Listen for system preference changes
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
            if (e.matches) this.enable();
            else this.disable();
        });
    }
    
    toggle() {
        if (this.isDark) {
            this.disable();
        } else {
            this.enable();
        }
    }
    
    enable() {
        this.html.classList.add('dark');
        this.isDark = true;
        localStorage.setItem('darkMode', 'true');
    }
    
    disable() {
        this.html.classList.remove('dark');
        this.isDark = false;
        localStorage.setItem('darkMode', 'false');
    }
}

// Sidebar Navigation Management
class Navigation {
    constructor() {
        this.toggleButton = document.querySelector('[data-drawer-toggle]');
        this.sidebar = document.querySelector('aside');
        this.navLinks = document.querySelectorAll('aside a');
        
        this.init();
    }
    
    init() {
        if (this.toggleButton && this.sidebar) {
            this.toggleButton.addEventListener('click', () => this.toggleSidebar());
        }
        
        // Close sidebar on link click (mobile)
        this.navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth < 768) {
                    this.closeSidebar();
                }
            });
        });
        
        // Highlight active link
        this.updateActiveLink();
        
        // Update on window resize
        window.addEventListener('resize', () => this.updateActiveLink());
    }
    
    toggleSidebar() {
        if (this.sidebar?.classList.contains('-translate-x-full')) {
            this.openSidebar();
        } else {
            this.closeSidebar();
        }
    }
    
    openSidebar() {
        this.sidebar?.classList.remove('-translate-x-full');
        this.sidebar?.classList.add('translate-x-0');
        document.body.style.overflow = 'hidden';
    }
    
    closeSidebar() {
        this.sidebar?.classList.add('-translate-x-full');
        this.sidebar?.classList.remove('translate-x-0');
        document.body.style.overflow = '';
    }
    
    updateActiveLink() {
        const currentPath = window.location.pathname;
        
        this.navLinks.forEach(link => {
            const href = link.getAttribute('href');
            const isActive = href === currentPath;
            
            if (isActive) {
                link.classList.add('bg-blue-50', 'dark:bg-blue-900', 'active');
                link.classList.remove('hover:bg-gray-100', 'dark:hover:bg-gray-700');
            } else {
                link.classList.remove('bg-blue-50', 'dark:bg-blue-900', 'active');
                link.classList.add('hover:bg-gray-100', 'dark:hover:bg-gray-700');
            }
        });
    }
}

// Notifications & Alerts
class NotificationManager {
    static showSuccess(message, duration = 3000) {
        this.show(message, 'success', duration);
    }
    
    static showError(message, duration = 4000) {
        this.show(message, 'danger', duration);
    }
    
    static showInfo(message, duration = 3000) {
        this.show(message, 'primary', duration);
    }
    
    static show(message, type = 'primary', duration = 3000) {
        const id = 'notification-' + Date.now();
        const colors = {
            success: 'bg-green-100 text-green-800 border-l-4 border-green-500',
            danger: 'bg-red-100 text-red-800 border-l-4 border-red-500',
            primary: 'bg-blue-100 text-blue-800 border-l-4 border-blue-500',
            warning: 'bg-yellow-100 text-yellow-800 border-l-4 border-yellow-500'
        };
        
        const html = `
            <div id="${id}" class="fixed top-5 right-5 max-w-sm p-4 rounded-lg shadow-lg ${colors[type]} animate-slideDown z-50">
                <p class="font-medium">${message}</p>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', html);
        
        setTimeout(() => {
            const el = document.getElementById(id);
            if (el) {
                el.style.opacity = '0';
                el.style.transition = 'opacity 300ms ease';
                setTimeout(() => el.remove(), 300);
            }
        }, duration);
    }
}

// Modal Manager
class ModalManager {
    static open(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.remove('hidden');
            modal.classList.add('show');
            document.body.style.overflow = 'hidden';
        }
    }
    
    static close(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.add('hidden');
            modal.classList.remove('show');
            document.body.style.overflow = '';
        }
    }
    
    static closeOnBackdropClick(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    this.close(modalId);
                }
            });
        }
    }
}

// Smooth Scroll Behavior
class SmoothScroll {
    static init() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    }
}

// Number Animation
class NumberAnimation {
    static animateValue(element, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            element.innerText = Math.floor(progress * (end - start) + start).toLocaleString();
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }
    
    static init() {
        document.querySelectorAll('[data-animate-number]').forEach(el => {
            const target = parseInt(el.dataset.animateNumber);
            const observer = new IntersectionObserver(([entry]) => {
                if (entry.isIntersecting) {
                    this.animateValue(el, 0, target, 1000);
                    observer.unobserve(el);
                }
            });
            observer.observe(el);
        });
    }
}

// Initialize everything on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    // Initialize all modules
    new DarkMode();
    new Navigation();
    
    SmoothScroll.init();
    NumberAnimation.init();
    
    // Close modal on backdrop click
    document.querySelectorAll('[data-modal]').forEach(modal => {
        ModalManager.closeOnBackdropClick(modal.id);
    });
});

// Export for use in other scripts
window.DarkMode = DarkMode;
window.Navigation = Navigation;
window.ModalManager = ModalManager;
window.NotificationManager = NotificationManager;
window.NumberAnimation = NumberAnimation;
