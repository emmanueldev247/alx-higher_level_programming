#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, response, body) => {
  if (err) { return; }

  for (const character of JSON.parse(body).characters) {
    request.get(character, (err, response, body) => {
      if (err) { console.log(err); }
      console.log(JSON.parse(body).name);
    });
  }
});
