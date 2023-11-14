#!/usr/bin/node

function printX (proc) {
  const num = parseInt(proc[2]);

  if (!isNaN(num)) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
}

printX(process.argv);
