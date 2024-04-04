/* script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header */

$(document).ready(function () {
  const header = $('header');
  const updateHeader = $('DIV#update_header');

  updateHeader.click(function () {
    header.text('New Header!!!');
  });
});
