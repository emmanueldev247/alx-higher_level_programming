#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let output = '';
      for (let j = 0; j < this.width; j++) {
        output += c;
      }
      console.log(output);
    }
  }
}

module.exports = Square;
