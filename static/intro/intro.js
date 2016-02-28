$(document).ready(function () {
    var xsamples = $('.samples').offset().top;
    var xmembers = $('.members').offset().top;
    var xabout = $('.about').offset().top;
    var xcontact = $('.contact').offset().top;

    $(window).scroll(function (event) {
        var scrollheight = $(window).scrollTop();
        if (scrollheight < xsamples - 50 && scrollheight > 0) {

            $("#home-btn").addClass('active');
            $("#samples-btn").removeClass('active');
            $("#members-btn").removeClass('active');
            $("#about-us-btn").removeClass('active');
            $("#contact-us-btn").removeClass('active');
        }
        else if (scrollheight < xmembers - 50 && scrollheight >= xsamples - 50) {
            $("#samples-btn").addClass('active');
            $("#home-btn").removeClass('active');
            $("#members-btn").removeClass('active');
            $("#about-us-btn").removeClass('active');
            $("#contact-us-btn").removeClass('active');
        }
        else if (scrollheight < xabout - 50 && scrollheight >= xmembers - 50) {
            $("#members-btn").addClass('active');
            $("#home-btn").removeClass('active');
            $("#samples-btn").removeClass('active');
            $("#about-us-btn").removeClass('active');
            $("#contact-us-btn").removeClass('active');
        }
        else if (scrollheight <= xcontact - 50 && scrollheight >= xabout - 50) {
            $("#about-us-btn").addClass('active');
            $("#home-btn").removeClass('active');
            $("#samples-btn").removeClass('active');
            $("#members-btn").removeClass('active');
            $("#contact-us-btn").removeClass('active');
        }
        else if (scrollheight < 5000 && scrollheight > xcontact - 50) {
            $("#contact-us-btn").addClass('active');
            $("#home-btn").removeClass('active');
            $("#samples-btn").removeClass('active');
            $("#members-btn").removeClass('active');
            $("#about-us-btn").removeClass('active');
        }
    });

    //$('#home-btn').click(function () {
    //    $("#samples-btn").removeAttr('class');
    //    $("#members-btn").removeAttr('class');
    //    $("#about-us-btn").removeAttr('class');
    //    $("#contact-us-btn").removeAttr('class');
    //
    //});
    //
    //$('#samples-btn').click(function () {
    //    $("#home-btn").removeAttr('class');
    //    $("#members-btn").removeAttr('class');
    //    $("#about-us-btn").removeAttr('class');
    //    $("#contact-us-btn").removeAttr('class');
    //})
    //
    //$('#members-btn').click(function () {
    //    $("#home-btn").removeAttr('class');
    //    $("#samples-btn").removeAttr('class');
    //    $("#about-us-btn").removeAttr('class');
    //    $("#contact-us-btn").removeAttr('class');
    //})
    //
    //$('#about-us-btn').click(function () {
    //    $("#home-btn").removeAttr('class');
    //    $("#samples-btn").removeAttr('class');
    //    $("#members-btn").removeAttr('class');
    //    $("#contact-us-btn").removeAttr('class');
    //})
    //$('#contact-us-btn').click(function () {
    //    $("#home-btn").removeAttr('class');
    //    $("#samples-btn").removeAttr('class');
    //    $("#members-btn").removeAttr('class');
    //    $("#about-us-btn").removeAttr('class');
    //})
    //
    //$('#scroll-samples-js').click(function () {
    //    $("#home-btn").removeAttr('class');
    //    $("#members-btn").removeAttr('class');
    //    $("#about-us-btn").removeAttr('class');
    //    $("#contact-us-btn").removeAttr('class');
    //})
    //
    //$('#scroll-members-js').click(function () {
    //    $("#home-btn").removeAttr('class');
    //    $("#samples-btn").removeAttr('class');
    //    $("#about-us-btn").removeAttr('class');
    //    $("#contact-us-btn").removeAttr('class');
    //})
    //
    //$('#scroll-aboutus-js').click(function () {
    //    $("#home-btn").removeAttr('class');
    //    $("#samples-btn").removeAttr('class');
    //    $("#members-btn").removeAttr('class');
    //    $("#contact-us-btn").removeAttr('class');
    //})
    //$('#scroll-contactus-js').click(function () {
    //    $("#home-btn").removeAttr('class');
    //    $("#samples-btn").removeAttr('class');
    //    $("#members-btn").removeAttr('class');
    //    $("#about-us-btn").removeAttr('class');
    //})


    var flag = false;

    $('.slider-left').click(function () {
        if (flag)
            return;

        flag = true;
        var $panel = $(this).parent().find('.slider-wrap');

        $panel.animate({scrollLeft: $panel.scrollLeft() - 400}, 500, function () {
            flag = false;
        });


    });
    /* on right button click scroll to
     the next sibling of the current visible slide */
    $('.slider-right').click(function () {
        if (flag)
            return;

        flag = true;
        var $panel = $(this).parent().find('.slider-wrap');

        $panel.animate({scrollLeft: $panel.scrollLeft() + 400}, 500, function () {
            flag = false;
        });

    });

    $('#home-btn').click(function () {
        $('html , body').animate({scrollTop: 0}, 1000);

    });

    $('#samples-btn, #scroll-samples-js').click(function () {
        $('html , body').animate({scrollTop: xsamples - 49}, 1000);

    });
    $('#members-btn , #scroll-members-js').click(function () {
        $('html , body').animate({scrollTop: xmembers - 49}, 1200);

    });

    $('#about-us-btn , #scroll-aboutus-js').click(function () {
        $('html , body').animate({scrollTop: xabout - 49}, 1500);

    });

    $('#contact-us-btn , #scroll-contactus-js').click(function () {
        var x = $(document).height();
        $('html , body').animate({scrollTop: x}, 2000);
    });


    $('.page-item').height($(window).height() - 65);


    var x = $(document).height();


    //CONTACT

    $('.send-btn').click(function () {
        $.ajax({
            type: 'POST',
            url: '/contact/',
            data: {
                'n': $('#contact-name').val(),
                'e': $('#contact-email').val(),
                't': $('#contact-title').val(),
                'te': $('#contact-text').val()

            },
            success: function (msg) {
                var res = msg.trim();

                if (res == 'OK') {
                    $('.contact .message').fadeIn();
                    $('#contact-name').val('');
                    $('#contact-email').val('');
                    $('#contact-title').val('');
                    $('#contact-text').val('');
                }
            }
        });
    });

});


$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

