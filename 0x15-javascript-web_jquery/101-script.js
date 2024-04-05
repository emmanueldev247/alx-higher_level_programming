/* script that adds, removes and clears LI elements from a list when the user clicks */

$(document).ready(() => {
  const item = '<li>Item</li>';
  const myList = $('UL.my_list');
  const addItem = $('DIV#add_item');
  const removeItem = $('DIV#remove_item');
  const clearList = $('DIV#clear_list');

  addItem.click(() => {
    myList.append(item);
  });

  removeItem.click(() => {
    myList.children().last().remove();
  });

  clearList.click(() => {
    myList.empty();
  });
});
