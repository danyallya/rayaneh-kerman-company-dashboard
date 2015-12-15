$(document).ready(function () {

    $('.slider-left').click(function () {


        var $panel = $(this).parent().find('.slider-wrap');

        $panel.animate({scrollLeft: $panel.scrollLeft() - 200}, 500);

    });
    /* on right button click scroll to
     the next sibling of the current visible slide */
    $('.slider-right').click(function () {

        var $panel = $(this).parent().find('.slider-wrap');

        $panel.animate({scrollLeft: $panel.scrollLeft() + 200}, 500);

    });

    $('#home-btn').click(function () {




        $('body').animate({scrollTop: 0}, 1000);

    });

    $('#samples-btn, #scroll-samples-js').click(function () {




        $('body').animate({scrollTop: 562}, 1000);

    });
    $('#members-btn , #scroll-members-js').click(function () {




        $('body').animate({scrollTop: 1081}, 1200);

    });

    $('#about-us-btn , #scroll-aboutus-js').click(function () {




        $('body').animate({scrollTop: 1602}, 1500);

    });

    $('#contact-us-btn , #scroll-contactus-js').click(function () {
        var x=$(document).height();
        console.log(x);



        $('body').animate({scrollTop: x}, 2000);

    });
    var x=$(document).height();
    console.log(x);

});

