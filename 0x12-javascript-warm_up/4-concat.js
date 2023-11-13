#!/usr/bin/node

function printArg (proc) {
  if (proc[2] && proc[3]) {
    console.log(`${proc[2]} is ${proc[3]}`);
  } else if (proc[2]) {
    console.log(`${proc[2]} is undefined`);
  } else {
    console.log('undefined is undefined');
  }
}

printArg(process.argv);
