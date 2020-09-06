$(document).ready(function () {
    // initializer for collapsible
    $('.collapsible').collapsible();
     // initializer for select
    $('select').formSelect();
    // initializer for datepicker
    $('.datepicker').datepicker();
    // initializer for modal
    $('.modal').modal();
    // initializer for flash message 
    $('.alert').fadeIn('slow', function () {
        $('.alert').delay(8000).fadeOut();
    });
    // initializer for sidenav
    $('.sidenav').sidenav();
    // initializer for share button
    $('.share_btn').click(function () {
        $('.toggle_button').toggleClass("active");
    })
});