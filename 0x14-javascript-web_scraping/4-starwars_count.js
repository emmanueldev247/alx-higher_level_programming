#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');

const url = process.argv[2];
const charID = 18;

request.get(url, (err, response, body) => {
  if (err) { return; }

  const data = JSON.parse(body);
  let count = 0;

  for (const result of data.results) {
    if (result.characters.some(element => element.includes(charID))) { count++; }
  }
  console.log(count);
});
