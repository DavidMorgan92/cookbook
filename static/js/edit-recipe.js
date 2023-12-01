$(document).ready(function () {
    // Turn first ingredient and step input fields into templates
    makeTemplate('#ingredients .input-field', 'ingredient-template', 'ingredient-template-input', 'ingredient-template-name');
    makeTemplate('#steps .input-field', 'step-template', 'step-template-input', 'step-template-name');

    // Update ingredient and step input labels
    setIngredientLabels();
    setStepLabels();

    // Set range slider labels
    setServesFromLabel();
    setServesToLabel();

    // On add ingredient button clicked
    $('#ingredients').on('click', '.add-btn', function () {
        // Clone the template
        const template = $('#ingredient-template').clone();

        // Un-hide it and remove its ID
        template
            .prop('hidden', false)
            .addClass('d-flex')
            .removeAttr('id');

        // Insert the template after the last ingredient
        template.insertAfter($('#ingredients .input-field').last());
        
        // Update ingredient input labels
        setIngredientLabels();
    });

    // On remove ingredient button clicked
    $('#ingredients').on('click', '.remove-btn', function () {
        // Remove this button's parent
        $(this).parent().remove();

        // Update ingredient input labels
        setIngredientLabels();
    });

    $('#steps').on('click', '.add-btn', function () {
        const template = $('#step-template').clone();

        template
            .prop('hidden', false)
            .addClass('d-flex')
            .removeAttr('id');

        $(this).parent().before(template);
        setStepLabels();
    });

    $('#steps').on('click', '.remove-btn', function () {
        $(this).parent().remove();
        setStepLabels();
    });

    // Update servers_from and serves_to labels when the values change
    $('#serves_from').on('change', setServesFromLabel);
    $('#serves_to').on('change', setServesToLabel);
});

function makeTemplate(selector, id, inputId, name) {
    // Turn first ingredients item into a hidden template
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

function setIngredientLabels() {
    // For each ingredient input field which is not hidden
    $('#ingredients .input-field:not(:hidden)').each(function (index) {
        // Create an ID with the input field's index
        const inputId = `ingredients-${index}`;

        // Set the ID and name of the input
        $(this).find('input')
            .attr('id', inputId)
            .attr('name', inputId);

        // Set the for attribute and the text of the label
        $(this).find('label')
            .attr('for', inputId)
            .text(`Ingredient ${index + 1}`);
    });
}

function setStepLabels() {
    $('#steps .input-field:not(:hidden)').each(function (index) {
        const inputId = `steps-${index}`;

        $(this).find('input')
            .attr('id', inputId)
            .attr('name', inputId);

        $(this).find('label')
            .attr('for', inputId)
            .text(`Step ${index + 1}`);
    });
}

function setServesFromLabel() {
    $('#serves_from').siblings('label').text(`Serves From ${$('#serves_from').val()}`);
}

function setServesToLabel() {
    $('#serves_to').siblings('label').text(`Serves To ${$('#serves_to').val()}`);
}
