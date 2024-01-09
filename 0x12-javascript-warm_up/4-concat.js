#!/usr/bin/node
const numArgs = process.argv.length - 2;
if (!process.argv[3]) {
  console.log('No argument');
} else {
  console.log(`${process.argv[3]}`);
}
