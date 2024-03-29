#!/usr/bin/node
// script that writes a string to a file

const fs = require('fs');

const file = process.argv[2];
const myData = process.argv[3];

fs.writeFile(file, myData, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
