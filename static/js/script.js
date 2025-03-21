// Header mobile menu functionality
document.addEventListener('DOMContentLoaded', function() {
  const mobileMenuBtns = document.querySelectorAll('.mobile-menu-btn');
  const navMenus = document.querySelectorAll('.nav-menu');

  mobileMenuBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      const navMenu = this.closest('.header').querySelector('.nav-menu');
      navMenu.classList.toggle('active');
      document.body.classList.toggle('menu-open');
    });
  });

  // Close menu when clicking outside
  document.addEventListener('click', function(event) {
    navMenus.forEach(navMenu => {
      const mobileMenuBtn = navMenu.closest('.header').querySelector('.mobile-menu-btn');
      if (!navMenu.contains(event.target) && !mobileMenuBtn.contains(event.target)) {
        navMenu.classList.remove('active');
        document.body.classList.remove('menu-open');
      }
    });
  });
}); 