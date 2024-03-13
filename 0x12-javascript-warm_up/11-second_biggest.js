#!/usr/bin/node

// Check if there are no arguments or only one argument
if (process.argv.length <= 2) {
  console.log(0); // Print 0 and exit
} else if (process.argv.length === 3) {
  console.log(0); // Print 0 and exit
} else {
  // If there are more than three arguments
  // Convert arguments to integers and store them in an array
  const numbers = process.argv.slice(2).map(Number);
  // Sort the array in descending order
  const sortedNumbers = numbers.sort((a, b) => b - a);
  // Print the second largest integer
  console.log(sortedNumbers[1]);
}
