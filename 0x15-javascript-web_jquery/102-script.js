/* script that fetches and prints how to say “Hello” depending on the language */

$(document).ready(() => {
  const langBox = $('INPUT#language_code');
  const translateBtn = $('INPUT#btn_translate');
  const helloDiv = $('DIV#hello');

  translateBtn.click(() => {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + langBox.val().trim();

    $.ajax({
      type: 'GET',
      dataType: 'json',
      url: url,
      success: function (data) {
        helloDiv.html('<span>' + data.hello + '</span>');
      }
    });
  });
});
