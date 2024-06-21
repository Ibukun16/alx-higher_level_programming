#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let c = 0; c < this.height; c++) {
      let a = '';
      for (let n = 0; n < this.width; n++) {
        a += 'X';
      }
      console.log(a);
    }
  }
}

module.exports = Rectangle;
