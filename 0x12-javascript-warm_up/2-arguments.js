#!/usr/bin/node
const process = require('process');
const numberOfArgs = process.argv.length;
if (numberOfArgs <= 2) {
  console.log('No argument');
} else if (numberOfArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
