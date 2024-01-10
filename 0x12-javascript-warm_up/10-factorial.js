#!/usr/bin/node
let x = process.argv[2];
x = parseInt(x);

console.log(factorial(x));

function factorial (a) {
  if (a === 0 || a === 1 || isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1);
}
