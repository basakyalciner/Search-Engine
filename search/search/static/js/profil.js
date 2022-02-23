$(document).ready(function(){
    //FOOTER SOCIAL BAR ANIMATION START
   $(".social-bar li").mouseenter(function(){
       $(this).removeClass("animation2");
      $(this).addClass("animation");
   });
    $(".social-bar li").mouseleave(function(){
        $(this).removeClass("animation");
      $(this).addClass("animation2");
   });
//FOOTER SOCIAL BAR ANIMATION END
//RATING START
$(".my-rating").starRating({
  initialRating: 4,
  strokeColor: '#894A00',
  strokeWidth: 10,
  starSize: 25
});
//RATING END
    
});