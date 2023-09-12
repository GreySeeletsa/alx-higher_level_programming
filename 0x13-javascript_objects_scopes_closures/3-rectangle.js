#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let b = '';
      for (let y = 0; y < this.width; y++) {
        b += 'X';
      }
      console.log(b);
    }
  }
}
module.exports = Rectangle;
