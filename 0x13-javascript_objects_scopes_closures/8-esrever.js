#!/usr/bin/node
exports.esrever = function (list) {
  let lgth = list.length - 1;
  let a = 0;
  while ((lgth - a) > 0) {
    const b = list[lgth];
    list[lgth] = list[a];
    list[a] = b;
    a++;
    lgth--;
  }
  return list;
};
