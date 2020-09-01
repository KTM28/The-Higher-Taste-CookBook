$(document).ready(function () {
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.datepicker').datepicker();
    $('.modal').modal();
    $('.alert').fadeIn('slow', function () {
        $('.alert').delay(8000).fadeOut();
    });
    $('.sidenav').sidenav();
});