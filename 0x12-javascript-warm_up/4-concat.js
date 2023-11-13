#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 2) {
  console.log('no args');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
