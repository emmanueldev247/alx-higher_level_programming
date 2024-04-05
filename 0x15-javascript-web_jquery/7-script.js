/* script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json */

const character = $('DIV#character');
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  const name = data.name;
  character.text(name);
});

/* --- THIS WORKS TOO --
$.ajax({
    type:  'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function(data) {
        const name = data.name;
        character.text(name);
    }
 });
 */
