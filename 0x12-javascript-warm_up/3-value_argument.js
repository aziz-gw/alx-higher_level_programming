#!/usr/bin/node

function printArg (proc) {
  if (!proc[2]) {
    console.log('No argument');
  } else {
    console.log(proc[2]);
  }
}

printArg(process.argv);
