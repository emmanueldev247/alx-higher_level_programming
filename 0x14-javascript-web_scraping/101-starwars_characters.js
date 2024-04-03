#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, response, body) => {
  if (err) { return; }

  const characters = JSON.parse(body).characters;

  (async () => {
    for (let i = 0; i < characters.length; i++) {
      console.log(await getCharacterName(characters[i]));
    }
  })();
});

async function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (err, response, body) => {
      if (err) {
        reject(err);
        return;
      }

      resolve(JSON.parse(body).name);
    });
  });
}
