
//percent of project
$(document).ready(function () {
    $('#example1').progress();
})

$(document).ready(function () {

    $('.slider-left').click(function () {


        var $panel = $(this).parent().parent().find('.slider-wrap');

        $panel.animate({scrollLeft: $panel.scrollLeft() - 102}, 500);

    });
    /* on right button click scroll to
     the next sibling of the current visible slide */
    $('.slider-right').click(function () {

        var $panel = $(this).parent().parent().find('.slider-wrap');

        $panel.animate({scrollLeft: $panel.scrollLeft() + 102}, 500);

    });
})