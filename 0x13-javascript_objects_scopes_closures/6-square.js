#!/usr/bin/node
const SquareN = require('./5-square');

class Square extends SquareN {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let n = 0; n < this.height; n++) {
      let p = '';
      for (let l = 0; l < this.width; l++) {
        p += c;
      }
      console.log(p);
    }
  }
}

module.exports = Square;
