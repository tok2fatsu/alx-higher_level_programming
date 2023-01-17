#!/usr/bin/node

const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fileStream = require('fs');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fileStream.writeFile(file, body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
