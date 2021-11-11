$(window).scroll(function() {
  if ($(this).scrollTop() < 200) {
    $("footer").slideUp();
      }
  else {
    $("footer").slideDown();
      }
});