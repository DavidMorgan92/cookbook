$(document).ready(function () {
    // Initialize mobile side-nav menu
    $('.sidenav').sidenav();

    // Initialize logout nav menu buttons to submit the hidden logout form
    $('.logout-button').on('click', function () {
        $("#logout-form").submit();
    });
});
