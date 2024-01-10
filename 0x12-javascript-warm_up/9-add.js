#!/usr/bin/node
let x = process.argv[2];
x = parseInt(x);
let y = process.argv[3];
y = parseInt(y);

console.log(add(x, y));

function add (a, b) {
  return a + b;
}
