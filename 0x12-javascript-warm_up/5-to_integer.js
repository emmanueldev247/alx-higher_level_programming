#!/usr/bin/node
const arg1 = process.argv[2];
const argInt = parseInt(arg1);
if (!isNaN(argInt)) {
  console.log('My number: ' + parseInt(arg1));
} else {
  console.log('Not a number');
}
