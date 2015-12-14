$(document).ready(function () {
//slider1
    $('.slider-operation-left').click(function () {

console.log(2);
        var $panel = $(this).parent().parent().find('.slider-opreration');

        $panel.animate({scrollLeft: $panel.scrollLeft() - 377.54}, 500);

    });
    /* on right button click scroll to
     the next sibling of the current visible slide */
    $('.slider-operation-right').click(function () {

        var $panel = $(this).parent().parent().find('.slider-opreration');

        $panel.animate({scrollLeft: $panel.scrollLeft() + 377.54}, 500);

    });


})

