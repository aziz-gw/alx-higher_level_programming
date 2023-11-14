#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

function printAdd (proc) {
  const num1 = parseInt(proc[2]);
  const num2 = parseInt(proc[3]);

  if (!isNaN(num1) && !isNaN(num2)) {
    const result = add(num1, num2);
    console.log(result);
  } else {
    console.log('NaN');
  }
}

printAdd(process.argv);
