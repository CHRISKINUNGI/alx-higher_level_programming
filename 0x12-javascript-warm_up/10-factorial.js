#!/usr/bin/node
function factorial (passedInteger) {
  const myInteger = parseInt(passedInteger);

  if (isNaN(myInteger)) {
    return 1;
  } else if (myInteger === 0 || myInteger === 1) {
    return 1;
  } else {
    return myInteger * factorial(myInteger - 1);
  }
}
console.log(factorial(process.argv[2]));
