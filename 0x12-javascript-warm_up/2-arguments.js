#!/usr/bin/node

function printArg (proc) {
  if (proc.length <= 2) {
    console.log('No argument');
  } else if (proc.length === 3) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}

printArg(process.argv);
