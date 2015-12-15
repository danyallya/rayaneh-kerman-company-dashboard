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
        var x = $(document).height();


        $('body').animate({scrollTop: x}, 2000);

    });
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

