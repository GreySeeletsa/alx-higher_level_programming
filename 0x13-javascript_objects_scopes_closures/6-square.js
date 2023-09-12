#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      let b = '';
      for (let y = 0; y < this.width; y++) {
        b += c;
      }
      console.log(b);
    }
  }
}
module.exports = Square;
