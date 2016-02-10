$(document).ready(function () {
    var xsamples = $('.samples-header').offset().top;
    var xmembers = $('.members-header').offset().top;
    var xabout = $('.about-header').offset().top;
    var xcontact = $('.contact-header').offset().top;

    $(window).scroll(function (event) {
        var scrollheight = $(window).scrollTop();
        if (scrollheight < xsamples - 66 && scrollheight > 0) {

            $("#home-btn").addClass('tab-current');
            $("#samples-btn").removeAttr('class');
            $("#members-btn").removeAttr('class');
            $("#about-us-btn").removeAttr('class');
            $("#contact-us-btn").removeAttr('class');
        }
        else if (scrollheight < xmembers - 66 && scrollheight >= xsamples - 66) {
            $("#samples-btn").addClass('tab-current');
            $("#home-btn").removeAttr('class');
            $("#members-btn").removeAttr('class');
            $("#about-us-btn").removeAttr('class');
            $("#contact-us-btn").removeAttr('class');
        }
        else if (scrollheight < xabout - 66 && scrollheight >= xmembers - 66) {
            $("#members-btn").addClass('tab-current');
            $("#home-btn").removeAttr('class');
            $("#samples-btn").removeAttr('class');
            $("#about-us-btn").removeAttr('class');
            $("#contact-us-btn").removeAttr('class');
        }
        else if (scrollheight <= xcontact - 65 && scrollheight >= xabout - 66) {
            $("#about-us-btn").addClass('tab-current');
            $("#home-btn").removeAttr('class');
            $("#samples-btn").removeAttr('class');
            $("#members-btn").removeAttr('class');
            $("#contact-us-btn").removeAttr('class');
        }
        else if (scrollheight < 3000 && scrollheight > xcontact - 65) {
            $("#contact-us-btn").addClass('tab-current');
            $("#home-btn").removeAttr('class');
            $("#samples-btn").removeAttr('class');
            $("#members-btn").removeAttr('class');
            $("#about-us-btn").removeAttr('class');
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


    $('.slider-left').click(function () {


        var $panel = $(this).parent().find('.slider-wrap');

        $panel.animate({scrollLeft: $panel.scrollLeft() - 400}, 500);

    });
    /* on right button click scroll to
     the next sibling of the current visible slide */
    $('.slider-right').click(function () {

        var $panel = $(this).parent().find('.slider-wrap');

        $panel.animate({scrollLeft: $panel.scrollLeft() + 400}, 500);

    });

    $('#home-btn').click(function () {
        $('body').animate({scrollTop: 0}, 1000);

    });

    $('#samples-btn, #scroll-samples-js').click(function () {
        $('body').animate({scrollTop: xsamples - 65}, 1000);

    });
    $('#members-btn , #scroll-members-js').click(function () {
        $('body').animate({scrollTop: xmembers - 65}, 1200);

    });

    $('#about-us-btn , #scroll-aboutus-js').click(function () {
        $('body').animate({scrollTop: xabout - 65}, 1500);

    });

    $('#contact-us-btn , #scroll-contactus-js').click(function () {
        var x = $(document).height();
        $('body').animate({scrollTop: x}, 2000);
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

