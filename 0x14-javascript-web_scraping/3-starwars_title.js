#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

const url = baseUrl + id;

request.get(url, (err, response, body) => {
  if (err) { return; }

  const data = JSON.parse(body);
  console.log(data.title);
});
