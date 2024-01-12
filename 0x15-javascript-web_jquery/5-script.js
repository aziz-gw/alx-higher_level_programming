const addEl = $('#add_item');

addEl.click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
