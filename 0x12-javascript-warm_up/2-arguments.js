#!/usr/bin/node

function printMsg (proc) {
  if (proc.length <= 2) {
    console.log('No argument');
  } else if (proc.length === 3) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}

printMsg(process.argv);
