#!/usr/bin/node
const myArgs = process.argv[2];
const sqrSize = parseInt(myArgs);

if (isNaN(sqrSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqrSize; i++) {
    let sqrLength = '';
    for (let j = 0; j < sqrSize; j++) {
      sqrLength += 'x';
    }
    console.log(sqrLength);
  }
}
/*
 * for (let i = 0; i < sqrSize; i++) {
 * let sqrLength = 'x'.repeat(sqrSize).trim();
* console.log(sqrLength)
*
 * }
 */
