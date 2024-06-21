#!/usr/bin/node
exports.callMeMoby = function (n, theFunction) {
  for (let c = 0; c < n; c++) {
    theFunction();
  }
};
