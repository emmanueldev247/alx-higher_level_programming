/* script that fetches and prints how to say “Hello” depending on the language */

$(document).ready(() => {
  const translateBtn = $('INPUT#btn_translate');
  const helloDiv = $('DIV#hello');
  const langBox = $('INPUT#language_code');

  translateBtn.click(helloAPI);

  translateBtn.keypress(function (event) {
    if (event.keyCode === 13) {
      helloAPI();
    }
  });

  function helloAPI () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + langBox.val().trim();
    $.ajax({
      type: 'GET',
      dataType: 'json',
      url: url,
      success: function (data) {
        helloDiv.html('<span>' + data.hello + '</span>');
      }
    });
  }
});
