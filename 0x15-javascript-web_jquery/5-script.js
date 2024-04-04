/* script that adds a <li> element to a list when the user clicks on the tag DIV#add_item */

$(document).ready(function () {
  const addItem = $('DIV#add_item');
  const myList = $('UL.my_list');

  addItem.click(function () {
    myList.append('<li>Item</li>');
  });
});
