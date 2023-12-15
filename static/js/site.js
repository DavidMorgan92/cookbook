$(document).ready(function () {
    // Initialize mobile side-nav menu
    $('.sidenav').sidenav();

    // Initialize character counters
    $('.character-counter').characterCounter();

    // Initialize select inputs
    $('select').formSelect();

    // Flex box input fields should have their character counter spans moved outside the input field div
    $('.input-field.d-flex').each(function () {
        $(this).after($(this).children('span.character-counter'));
    });

    // Initialize logout nav menu buttons to submit the hidden logout form
    $('.logout-button').on('click', function () {
        $("#logout-form").submit();
    });
});
