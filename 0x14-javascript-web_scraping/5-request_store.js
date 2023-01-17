#!/usr/bin/node

const request = require('request');
const filePath = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    filePath.writeFile(file, body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
