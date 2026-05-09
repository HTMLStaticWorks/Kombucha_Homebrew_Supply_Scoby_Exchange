// Main JavaScript for Kombucha Website

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');

  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });
  }

  // Dark/Light Mode Toggle
  const themeToggleBtns = document.querySelectorAll('.theme-toggle');
  const htmlElement = document.documentElement;
  
  // Check local storage or system preference
  if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    htmlElement.classList.add('dark');
  } else {
    htmlElement.classList.remove('dark');
  }

  themeToggleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      htmlElement.classList.toggle('dark');
      if (htmlElement.classList.contains('dark')) {
        localStorage.theme = 'dark';
      } else {
        localStorage.theme = 'light';
      }
    });
  });

  // RTL Toggle
  const rtlToggleBtns = document.querySelectorAll('.rtl-toggle');
  
  const updateRtlButtons = (isRtl) => {
    rtlToggleBtns.forEach(btn => {
      btn.innerText = isRtl ? 'LTR' : 'RTL';
    });
  };

  if (localStorage.rtl === 'true') {
    htmlElement.setAttribute('dir', 'rtl');
    updateRtlButtons(true);
  } else {
    updateRtlButtons(false);
  }

  rtlToggleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const isRtl = htmlElement.getAttribute('dir') === 'rtl';
      if (isRtl) {
        htmlElement.removeAttribute('dir');
        localStorage.rtl = 'false';
        updateRtlButtons(false);
      } else {
        htmlElement.setAttribute('dir', 'rtl');
        localStorage.rtl = 'true';
        updateRtlButtons(true);
      }
    });
  });

  // Scroll to Top Button Logic
  const scrollTopBtn = document.getElementById('scroll-to-top');
  
  if (scrollTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        scrollTopBtn.classList.add('show');
      } else {
        scrollTopBtn.classList.remove('show');
      }
    });

    scrollTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // Fade Up Animation Observer
  const fadeUpElements = document.querySelectorAll('.fade-up');
  
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  fadeUpElements.forEach(el => {
    observer.observe(el);
  });

  // Cart Drawer Logic
  const cartBtns = document.querySelectorAll('.cart-btn-trigger');
  const cartDrawer = document.getElementById('cart-drawer');
  const cartOverlay = document.getElementById('cart-overlay');
  const closeCart = document.getElementById('close-cart');
  const startShopping = document.getElementById('start-shopping');

  const toggleCart = (show) => {
    if (show) {
      cartOverlay.classList.remove('hidden');
      setTimeout(() => {
        cartOverlay.classList.add('opacity-100');
        cartDrawer.style.right = '0';
      }, 10);
      document.body.style.overflow = 'hidden';
    } else {
      cartDrawer.style.right = '-100%';
      cartOverlay.classList.remove('opacity-100');
      setTimeout(() => {
        cartOverlay.classList.add('hidden');
      }, 300);
      document.body.style.overflow = '';
    }
  };

  if (cartBtns.length > 0 && cartDrawer && cartOverlay) {
    cartBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        toggleCart(true);
      });
    });
    closeCart.addEventListener('click', () => toggleCart(false));
    cartOverlay.addEventListener('click', () => toggleCart(false));
    if (startShopping) startShopping.addEventListener('click', () => toggleCart(false));
  }

  // Basic Add to Cart Simulation
  const quickAddBtns = document.querySelectorAll('.group button.bg-white.text-charcoal'); // Select the Quick Add buttons on cards
  let itemsInCart = 0;

  quickAddBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      itemsInCart++;
      const cartCounts = document.querySelectorAll('.cart-count');
      cartCounts.forEach(count => {
        count.innerText = itemsInCart;
        count.classList.add('scale-125');
        setTimeout(() => count.classList.remove('scale-125'), 200);
      });
      
      // Optional: show a mini toast or open cart
      // toggleCart(true); 
    });
  });

  // Sticky Header
  const header = document.getElementById('main-header');
  if (header) {
    const hasInitialWhiteText = header.classList.contains('text-white');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('shadow-md', 'glass', 'py-2');
        header.classList.remove('bg-transparent', 'py-4');
        if (hasInitialWhiteText) header.classList.remove('text-white');
      } else {
        header.classList.remove('shadow-md', 'glass', 'py-2');
        header.classList.add('bg-transparent', 'py-4');
        if (hasInitialWhiteText) header.classList.add('text-white');
      }
    });
  }
});
