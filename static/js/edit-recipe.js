$(document).ready(function () {
    // Turn first ingredient and step input fields into templates
    makeTemplate('#ingredients .input-field', 'ingredient-template', 'ingredient-template-input', 'ingredient-template-name');
    makeTemplate('#steps .input-field', 'step-template', 'step-template-input', 'step-template-name');

    // Update ingredient and step input labels
    setFieldListLabels('#ingredients', 'ingredients', 'Ingredient');
    setFieldListLabels('#steps', 'steps', 'Step');

    // Set range slider labels
    setRangeLabel('Serves from', '#serves_from');
    setRangeLabel('Serves to', '#serves_to');

    // Setup add/remove buttons
    setupAddRemoveButtons('#ingredients', '#ingredient-template', () => setFieldListLabels('#ingredients', 'ingredients', 'Ingredient'));
    setupAddRemoveButtons('#steps', '#step-template', () => setFieldListLabels('#steps', 'steps', 'Step'));

    // Update serves_from and serves_to labels when the values change
    $('#serves_from').on('change', () => setRangeLabel('Serves from', '#serves_from'));
    $('#serves_to').on('change', () => setRangeLabel('Serves to', '#serves_to'));

    // Show edit-image-form and hide edit-image-button when edit-image-button is clicked
    $('#edit-image-button').on('click', function () {
        $('#edit-image-button').hide();
        $('#edit-image-form').prop('hidden', false);
    });

    // Show edit-image-button and hide edit-image-form when cancel-edit-image-button is clicked
    $('#cancel-edit-image-button').on('click', function (event) {
        // Prevent form submission when cancel button is clicked
        event.preventDefault();
        
        $('#edit-image-button').show();
        $('#edit-image-form').prop('hidden', true);
    });
});

function setupAddRemoveButtons(sectionId, templateId, callback) {
    // On add button clicked
    $(sectionId).on('click', '.add-btn', function () {
        // Clone the template
        const template = $(templateId).clone();

        // Un-hide it and remove its ID
        template
            .prop('hidden', false)
            .addClass('d-flex')
            .removeAttr('id');

        // Append the template to the controls div
        template.appendTo($(sectionId).children('.controls'));

        // Invoke callback
        callback();
    });

    // On remove button clicked
    $(sectionId).on('click', '.remove-btn', function () {
        // Remove this button's parent
        $(this).parent().remove();

        // Invoke callback
        callback();
    });
}

function makeTemplate(selector, id, inputId, name) {
    // Get first element which matches the selector
    const firstIngredient = $(selector).first();

    // Hide the template and give it an ID
    firstIngredient
        .prop('hidden', true)
        .removeClass('d-flex')
        .attr('id', id);

    // Set the ID and name attributes of the template input
    firstIngredient.find('input')
        .attr('id', inputId)
        .attr('name', name);

    // Set the for attribute of the template label
    firstIngredient.find('label')
        .attr('for', inputId);

    // Move the template to outside the edit form
    firstIngredient.insertAfter('#edit-form');
}

function setFieldListLabels(selector, idPrefix, labelPrefix) {
    // For each input-field in the selector which is not hidden
    $(`${selector} .input-field:not(:hidden)`).each(function (index) {
        // Create an ID for this input
        const inputId = `${idPrefix}-${index}`;

        // Assign the ID and name to the input
        $(this).find('input')
            .attr('id', inputId)
            .attr('name', inputId);

        // Set the for attribute and text of the label
        $(this).find('label')
            .attr('for', inputId)
            .text(`${labelPrefix} ${index + 1}`);
    });
}

function setRangeLabel(labelPrefix, input) {
    // Set label of the range input to display its value
    $(input).siblings('label').text(`${labelPrefix} ${$(input).val()}`);
}
