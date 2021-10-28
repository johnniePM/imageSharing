$(function(){
    $(document).scroll(function () {
        var $nav = $(".top-header");
        if (document.body.scrollTop >= 280 || document.documentElement.scrollTop >= 280) {
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
      }
      if($nav.hasClass('scrolled')){
       if (document.body.scrollTop < 280 || document.documentElement.scrollTop < 280){
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    }
      }
    }
      );
  });


