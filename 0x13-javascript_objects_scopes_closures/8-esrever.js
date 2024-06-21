#!/usr/bin/node
exports.esrever = function (list) {
  const revarray = [];
  for (let count = list.length - 1; count >= 0; count--) {
    revarray.push(list[count]);
  }
  return revarray;
};
