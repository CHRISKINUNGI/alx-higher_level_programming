#!/usr/bin/node
const myArgs = process.argv;

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
console.log(add(myArgs[2], myArgs[3]));
