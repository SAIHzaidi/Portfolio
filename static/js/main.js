// Animate progress bars when page loads
window.addEventListener('load', () => {
  setTimeout(() => {
    document.querySelectorAll('.metric-fill, .bar-fill').forEach(el => {
      const target = el.dataset.target;
      if (target) el.style.width = target + '%';
    });
  }, 200);
});

// Smooth scroll for nav links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Highlight active nav link on scroll
const sections = document.querySelectorAll('section[id], div[id]');
const navLinks = document.querySelectorAll('.nav-links a');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => {
        link.style.color = link.getAttribute('href') === '#' + entry.target.id
          ? '#fff'
          : 'rgba(255,255,255,0.5)';
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => observer.observe(s));
