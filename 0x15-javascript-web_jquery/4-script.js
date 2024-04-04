/* script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header */

$(document).ready(function () {
  const togHeader = $('DIV#toggle_header');
  const header = $('header');

  togHeader.on('click', function () {
    header.toggleClass('red green');
  });
});
