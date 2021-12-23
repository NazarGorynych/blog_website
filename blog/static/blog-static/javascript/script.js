
 $("body").on('click', ".follow, .unfollow", function (e) {
     e.preventDefault();
     $button = $(this);
     $button.toggleClass('unfollow').toggleClass('follow');
     $button.text($button.hasClass('follow') ? 'follow' : 'unfollow');
 });

//
// $(window).scroll(function() {
//   if ($(this).scrollTop() < 200) {
//     $("footer").slideUp();
//       }
//   else {
//     $("footer").slideDown();
//       }
// });