#!/usr/bin/node
const numArgs = process.argv.length;
if (numArgs < 4) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  let myList = args.map(arg => parseInt(arg));
  let maxNumber = Math.max(...myList);

  myList = myList.filter(number => number !== maxNumber);

  maxNumber = Math.max(...myList);
  console.log(maxNumber);
}
