#!/usr/bin/node
let new_arg = 0;

exports.logMe = function (item) {
  console.log(new_arg + ': ' + item);
  new_arg++;
};
