

$(document).ready(function() {
    $('#fullpage').fullpage({
        sectionsColor: ['#2CA3C1', '#2CA3C1', '#2CA3C1', '#2CA3C1','#2CA3C1' ,'#327a9e','#327a9e','#327a9e'],
        anchors: ['firstPage', 'secondPage', '3rdPage', '4thpage','5thpage','6thpage', 'lastpage','dsds'],
        menu: '#menu',
        navigation: true,
        navigationPosition: 'right',

        afterLoad: function(anchorLink, index){


            //section 1
            if(anchorLink =='firstPage'){
                //moving the image
                setTimeout(function () {
                    $('#section1').find('.intro').addClass("show");

                }, 500);
                //$('#section1').find('.intro').delay(500).animate({
                //    left: '0%.'
                //}, 1500, 'easeOutExpo');
            }
            if(anchorLink =='4thpage'){
                //moving the image
                setTimeout(function () {
                    $('#section3').find('.intro').addClass("show");
                    $('#section3').find('.intro1').addClass("show");

                }, 200);
                //$('#section1').find('.intro').delay(500).animate({
                //    left: '0%.'
                //}, 1500, 'easeOutExpo');
            }
            if(anchorLink =='5thpage'){
                //moving the image
                setTimeout(function () {
                    $('#section4').find('.intro').addClass("show");
                    $('#section4').find('.intro1').addClass("show");


                }, 200);
                //$('#section1').find('.intro').delay(500).animate({
                //    left: '0%.'
                //}, 1500, 'easeOutExpo');
            }
            if(anchorLink =='6thpage'){
                //moving the image
                setTimeout(function () {
                    $('#section5').find('.intro').addClass("show");
                    $('#section5').find('.intro1').addClass("show");


                }, 200);
                //$('#section1').find('.intro').delay(500).animate({
                //    left: '0%.'
                //}, 1500, 'easeOutExpo');
            }
            if(index == 3){
                $('#iphone3, #iphone2, #iphone4').addClass('active');
            }
            else
            {
                $('#iphone3, #iphone2, #iphone4').removeClass('active');
            }


        }
    });

});
