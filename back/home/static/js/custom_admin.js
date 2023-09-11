$(() => {
  const fields = $(
    ".w-panel__wrapper .w-field__wrapper .w-field--checkbox_select_multiple"
  );

  fields.each((index, field) => {
    const $field = $(field);
    const $parent = $field.closest(".w-panel__wrapper");
    const $label = $parent.find(".w-field__label");

    const $button = $(`
      <div class="w-custom__select-all-button">
        <button class="button button-small" type="button">Izberi vse/Odstrani izbiro vseh</button>
      </div>
    `);
    $button.on("click", onSelectAllClick);
    $label.append($button);
  });

  function onSelectAllClick(event) {
    const $button = $(event.target);
    const $parent = $button.closest(".w-panel__wrapper");
    const $field = $parent.find(".w-field--checkbox_select_multiple");
    const $checkboxes = $field.find("input[type=checkbox]");
    const $checked = $checkboxes.filter(":checked");

    if ($checked.length === $checkboxes.length) {
      $checkboxes.prop("checked", false);
    } else {
      $checkboxes.prop("checked", true);
    }
  }
});
