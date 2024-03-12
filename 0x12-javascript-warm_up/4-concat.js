#!/usr/bin/node

// Destructuring assignment to extract the second and third elements from process.argv
const [,, arg1, arg2] = process.argv;

// Using template literals to format the output
// If arg1 is undefined, use 'undefined', otherwise use its value
// If arg2 is undefined, use 'undefined', otherwise use its value
console.log(`${arg1 || 'undefined'} is ${arg2 || 'undefined'}`);
