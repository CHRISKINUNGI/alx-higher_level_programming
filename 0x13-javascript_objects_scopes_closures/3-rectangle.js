#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (this.isValidDimensions(w, h)) {
      this.width = w;
      this.height = h;
    }
  }

  isValidDimensions (width, height) {
    return width > 0 && height > 0 && Number.isInteger(width) && Number.isInteger(height);
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
