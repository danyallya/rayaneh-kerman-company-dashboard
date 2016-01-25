$(document).ready(function () {


    $('#add-Transaction-btn').click(function () {

        $('#Transaction-modal')
            .modal('show')
        ;
    });

    $('.cancel').click(function () {

        $('#Transaction-modal')
            .modal('hide')
        ;
    });


});
