/* script that updates the text color of the <header> element to red (#FF0000)
   when the user clicks on the tag DIV#red_header */

const redHeader = $('#red_header');

redHeader.on('click', function() {
    redHeader.css('color', '#FF0000');
 });
