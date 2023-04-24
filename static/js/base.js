$(document).ready(function() {
    new WOW().init();

    $(window).scroll(function() {

        var height = $('.navbar').height();
        var scrollTop = $(window).scrollTop();

        if (scrollTop >= height - 40) {
            $('.navbar').addClass('navbar-scrolled');

        } else {
            $('.navbar').removeClass('navbar-scrolled');
        }

    });
});

$(window).on('load', function () {
    $('#loader').hide();
  }) 

  $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
        $('.back-to-top').fadeIn('slow');
    } else {
        $('.back-to-top').fadeOut('slow');
    }
});
$('.back-to-top').click(function () {
    $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
    return false;
});


