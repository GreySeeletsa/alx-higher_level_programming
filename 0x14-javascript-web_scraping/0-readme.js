#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// The first arg is the file path
const file = process.argv[2];

fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
