const toggleDivEl = $('#toggle_header');
const headerColour = $('header');

toggleDivEl.click(function () {
  headerColour.toggleClass('red green');
});
