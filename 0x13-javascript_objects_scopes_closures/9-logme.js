#!/usr/bin/node
let logNumber = 0;

exports.logMe = function (item) {
  console.log(logNumber + ': ' + item);
  logNumber++;
};
