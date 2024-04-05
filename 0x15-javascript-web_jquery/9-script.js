/* script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
   and displays the value of hello from that fetch in the HTML tag DIV#hello */

$(function () {
  const divHello = $('DIV#hello');

  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      divHello.text(data.hello);
      console.log(data.hello);
    }
  });
});
