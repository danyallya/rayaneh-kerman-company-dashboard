
$(document).ready(function () {


    $('#add-account-btn').click(function () {

        $('#add-account-modal')
            .modal('show')
        ;
    });

    $('.cancel1').click(function () {

        $('#add-account-modal')
            .modal('hide')
        ;
    });


    $('#Transaction1-btn').click(function () {

        $('#Transaction1-modal')
            .modal('show')
        ;
    });

    $('.cancel').click(function () {

        $('#Transaction1-modal')
            .modal('hide')
        ;
    });

});