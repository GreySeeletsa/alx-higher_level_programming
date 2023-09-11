#!/usr/bin/node
function printMessage(...args) {
  const numArgs = args.length;
  if (numArgs === 0) {
    console.log('No argument');
  } else if (numArgs === 1) {
    console.log('Argument found');
  } else {
    console.log(numArgs + 'Arguments found');
  }
}
