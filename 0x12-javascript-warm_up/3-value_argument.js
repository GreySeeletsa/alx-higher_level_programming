#!/usr/bin/node
const fstArg = process.argv[2];

if (fstArg) {
  console.log(fstArg);
} else {
  console.log('No argument');
}
