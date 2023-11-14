#!/usr/bin/node

function printNum (proc) {
  const num = parseInt(proc[2]);

  if (!isNaN(num)) {
    console.log(`My number: ${num}`);
  } else {
    console.log('Not a number');
  }
}

printNum(process.argv);
