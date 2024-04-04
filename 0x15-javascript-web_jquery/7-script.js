/* script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json */

$(document).ready(function () {
  const character = $('DIV#character');
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    const name = data.name;

    character.text(name);
   });


});
