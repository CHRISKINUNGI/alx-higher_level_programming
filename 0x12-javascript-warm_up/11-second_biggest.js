#!/usr/bin/node
const argsLength = process.argv.length;
const passedIntegers = process.argv.slice(2);

if (argsLength <= 2 || argsLength === 3) {
  console.log(0);
} else {
  const sortedIntegers = passedIntegers.sort((a, b) => b - a);
  console.log(sortedIntegers[1]);
}
