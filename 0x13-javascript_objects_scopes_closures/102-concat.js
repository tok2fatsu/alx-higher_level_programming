#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (fs.existsSync(fileA) && fs.existsSync(fileB)) {
  fs.writeFileSync(fileC, fs.readFileSync(fileA));
  fs.appendFileSync(fileC, fs.readFileSync(fileB));
}
