$(document).ready(function () {
    $('#fullpage').fullpage({
        sectionsColor: ['#327a9e', '#327a9e', '#327a9e', '#327a9e', '#327a9e', '#327a9e', '#327a9e', '#327a9e'],
        anchors: ['firstPage', 'secondPage', '3rdPage', '4thpage', '5thpage', '6thpage', '7thpage', 'lastpage'],
        menu: '#menu',
        navigation: true,
        navigationPosition: 'right',
        afterLoad: function (anchorLink, index) {


            //section 1
            if (anchorLink == 'firstPage') {
                //moving the image
                setTimeout(function () {
                    $('#section1').find('.intro').addClass("show");

                }, 500);
                //$('#section1').find('.intro').delay(500).animate({
                //    left: '0%.'
                //}, 1500, 'easeOutExpo');
            }
            if (anchorLink == '4thpage') {
                //moving the image
                setTimeout(function () {
                    $('#section3').find('.intro').addClass("show");
                    $('#section3').find('.intro1').addClass("show");

                }, 200);
                //$('#section1').find('.intro').delay(500).animate({
                //    left: '0%.'
                //}, 1500, 'easeOutExpo');
            }
            if (anchorLink == '5thpage') {
                //moving the image
                setTimeout(function () {
                    $('#section4').find('.intro').addClass("show");
                    $('#section4').find('.intro1').addClass("show");


                }, 200);
                //$('#section1').find('.intro').delay(500).animate({
                //    left: '0%.'
                //}, 1500, 'easeOutExpo');
            }
            if (anchorLink == '6thpage') {
                //moving the image
                setTimeout(function () {
                    $('#section5').find('.intro').addClass("show");
                    $('#section5').find('.intro1').addClass("show");


                }, 200);
                //$('#section1').find('.intro').delay(500).animate({
                //    left: '0%.'
                //}, 1500, 'easeOutExpo');
            }
            if (anchorLink == '7thpage') {
                //moving the image
                setTimeout(function () {
                    $('#section7').find('.intro').addClass("show");
                    $('#section7').find('.intro1').addClass("show");

                }, 200);
                //$('#section1').find('.intro').delay(500).animate({
                //    left: '0%.'
                //}, 1500, 'easeOutExpo');
            }

            if (index == 3) {
                $('#iphone3, #iphone2, #iphone4').addClass('active');
            }
            else {
                $('#iphone3, #iphone2, #iphone4').removeClass('active');
            }


        }
    });


    //CONTACT

    $('.send-btn').click(function () {
        $.ajax({
            type: 'POST',
            url: '/contact/',
            data: {
                'e': $('#contact-email').val(),
                'te': $('#contact-text').val()

            },
            success: function (msg) {
                var res = msg.trim();

                if (res == 'OK') {
                    $('.contact.message').fadeIn();
                    $('#contact-email').val('');
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

