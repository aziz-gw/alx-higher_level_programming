#!/usr/bin/node

function secondBiggest (proc) {
  const nums = proc.slice(2).map(Number);

  if (nums.length < 2) {
    console.log('0');
  } else {
    const sortedNums = nums.sort((a, b) => b - a);
    console.log(sortedNums[1]);
  }
}

secondBiggest(process.argv);
