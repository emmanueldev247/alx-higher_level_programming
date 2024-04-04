/* script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header */

$(document).ready(function () {
  const redHeader = $('DIV#red_header');
  const header = $('header');

  redHeader.on('click', function () {
    header.addClass('red');
  });
});
