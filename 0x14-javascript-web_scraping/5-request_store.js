#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) { return; }

  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) { console.log(err); }
  });
});
