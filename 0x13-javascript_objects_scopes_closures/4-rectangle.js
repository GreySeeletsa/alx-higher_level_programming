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

  rotate () {
    const j = this.width;
    this.width = this.height;
    this.height = j;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
