#!/usr/bin/node
let x = process.argv[2];
x = parseInt(x);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let output = '';
    for (let j = 0; j < x; j++) {
      output += 'X';
    }
    console.log(output);
  }
}
