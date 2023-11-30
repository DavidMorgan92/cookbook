$(document).ready(function () {
    makeTemplates();
    setIngredientLabels();
    setStepLabels();

    $('#ingredients').on('click', '.add-btn', function () {
        const template = $('#ingredient-template').clone();
        template.prop('hidden', false).addClass('d-flex');
        $(this).parent().before(template);
        setIngredientLabels();
    });

    $('#ingredients').on('click', '.remove-btn', function () {
        $(this).parent().remove();
        setIngredientLabels();
    });

    $('#steps').on('click', '.add-btn', function () {
        const template = $('#step-template').clone();
        template.prop('hidden', false).addClass('d-flex');
        $(this).parent().before(template);
        setStepLabels();
    });

    $('#steps').on('click', '.remove-btn', function () {
        $(this).parent().remove();
        setStepLabels();
    });
});

function makeTemplates() {
    // Turn first ingredients item into a hidden template and give it a template ID
    const firstIngredient = $('#ingredients .input-field').first();

    firstIngredient
        .prop('hidden', true)
        .removeClass('d-flex')
        .attr('id', 'ingredient-template');

    firstIngredient.find('input')
        .attr('id', 'ingredient-template-input')
        .attr('name', 'ingredient-template-name');

    firstIngredient.find('label')
        .attr('for', 'ingredient-template-input');

    firstIngredient.insertAfter('form');

    // Turn first step item into a hidden template and give it a template ID
    const firstStep = $('#steps .input-field').first();

    firstStep
        .prop('hidden', true)
        .removeClass('d-flex')
        .attr('id', 'step-template');

    firstStep.find('input')
        .attr('id', 'step-template-input')
        .attr('name', 'step-template-name');

    firstStep.find('label')
        .attr('for', 'step-template-input');

    firstStep.insertAfter('form');
}

function setIngredientLabels() {
    $('#ingredients .input-field:not(:hidden)').each(function (index) {
        const inputId = `ingredients-${index}`;

        $(this).find('input')
            .attr('id', inputId)
            .attr('name', inputId);

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
