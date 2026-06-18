(function () {
  'use strict';

  var tg = typeof CHAT_LINK_TG !== 'undefined' ? CHAT_LINK_TG : '#';
  var max = typeof CHAT_LINK_MAX !== 'undefined' ? CHAT_LINK_MAX : '#';

  document.querySelectorAll('.chat-link--tg').forEach(function (link) {
    link.href = tg;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
  });

  document.querySelectorAll('.chat-link--max').forEach(function (link) {
    link.href = max;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
  });
  // Плавное появление блоков при прокрутке
  var reveals = document.querySelectorAll('.reveal:not(.is-visible)');
  if ('IntersectionObserver' in window && reveals.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );
    reveals.forEach(function (el) {
      observer.observe(el);
    });
  } else {
    reveals.forEach(function (el) {
      el.classList.add('is-visible');
    });
  }

  // FAQ-аккордеон
  document.querySelectorAll('.faq__question').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq__item');
      var isOpen = item.classList.contains('is-open');

      document.querySelectorAll('.faq__item.is-open').forEach(function (open) {
        open.classList.remove('is-open');
        open.querySelector('.faq__question').setAttribute('aria-expanded', 'false');
      });

      if (!isOpen) {
        item.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });
})();
