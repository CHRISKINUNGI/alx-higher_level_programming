#!/usr/bin/node
const myArgs = process.argv[2];
const sqrSize = parseInt(myArgs);

if (isNaN(sqrSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqrSize; i++) {
    const sqrLength = 'x'.repeat(sqrSize).trim();
    console.log(sqrLength);
  }
}
