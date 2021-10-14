$(function(){
    $(document).scroll(function () {
        var $nav = $(".top-header");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
      });
  });