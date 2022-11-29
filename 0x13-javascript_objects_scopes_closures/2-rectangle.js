#!/usr/bin/node
module.exports = class Rectangle {
  constructor (W, H) {
    if (W > 0 && H > 0) { [this.width, this.height] = [W, H]; }
  }
};
