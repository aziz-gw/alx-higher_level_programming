#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0) {
    return 1;
  }

  return n * factorial(n - 1);
}

function printFact (proc) {
  const num = parseInt(proc[2]);

  if (!isNaN(num)) {
    const result = factorial(num);
    console.log(result);
  } else {
    console.log('1');
  }
}

printFact(process.argv);
