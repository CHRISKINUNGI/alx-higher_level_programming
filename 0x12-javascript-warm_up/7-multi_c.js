#!/usr/bin/node
const process = require('process');
const times = parseInt(process.argv[2]);
if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('Cis fun');
  }
}
