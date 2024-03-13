0x12. JavaScript - Warm up:  
Javascript  

0. First constant, first print:  
mandatory    
Write a script that prints “JavaScript is amazing”:  
- You must create a constant variable called myVar with the value “JavaScript is amazing”  
- You must use console.log(...) to print all output  
- You are not allowed to use var  

1. 3 languages:  
mandatory    
Write a script that prints 3 lines:  
- The first line: “C is fun”  
- The second line: “Python is cool”  
- The third line: “JavaScript is amazing”  
- You must use console.log(...) to print all output  
- You are not allowed to use var  

2. Arguments:  
mandatory  
Write a script that prints a message depending of the number of arguments passed:  
- If no arguments are passed to the script, print “No argument”  
- If only one argument is passed to the script, print “Argument found”  
- Otherwise, print “Arguments found”  
- You must use console.log(...) to print all output  
- You are not allowed to use var  
Reference: process.argv (https://nodejs.org/api/process.html#process_process_argv)  

3. Value of my argument:  
mandatory  
Write a script that prints the first argument passed to it:  
- If no arguments are passed to the script, print “No argument”  
- You must use console.log(...) to print all output  
- You are not allowed to use var  
- You are not allowed to use length  

4. Create a sentence:  
mandatory  
Write a script that prints two arguments passed to it, in the following format: “ is ”  
- You must use console.log(...) to print all output  
- You are not allowed to use var  

5. An Integer:  
mandatory  
Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:  
- If the argument can’t be converted to an integer, print “Not a number”  
- You must use console.log(...) to print all output  
- You are not allowed to use var  
- You are not allowed to use try/catch  

6. Loop to languages:  
mandatory  
Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop  
- The first line: “C is fun”  
- The second line: “Python is cool”  
- The third line: “JavaScript is amazing”  
- You must use console.log(...) to print all output  
- You are not allowed to use var  
- You are not allowed to use any if/else statement  
- You can use only one console.log  
- You must use a loop (while, for, etc.)  

7. I love C:  
mandatory  
Write a script that prints x times “C is fun”  
- Where x is the first argument of the script  
- If the first argument can’t be converted to an integer, print “Missing number of occurrences”  
- You must use console.log(...) to print all output  
- You are not allowed to use var  
- You can use only two console.log  
- You must use a loop (while, for, etc.)  

8. Square  
mandatory  
Write a script that prints a square  
- The first argument is the size of the square  
- If the first argument can’t be converted to an integer, print “Missing size”  
- You must use the character X to print the square  
- You must use console.log(...) to print all output  
- You are not allowed to use var  
- You must use a loop (while, for, etc.)  

9. Add:  
mandatory  
Write a script that prints the addition of 2 integers  
- The first argument is the first integer  
- The second argument is the second integer  
- You have to define a function with this prototype: function add(a, b)  
- You must use console.log(...) to print all output  
- You are not allowed to use var  

10. Factorial:  
mandatory  
Write a script that computes and prints a factorial  
- The first argument is integer (argument can be cast as integer) used for computing the factorial  
- Factorial of NaN is 1  
- You must do it recursively  
- You must use a function  
- You must use console.log(...) to print all output  
- You are not allowed to use var  

11. Second biggest!:  
mandatory  
Write a script that searches the second biggest integer in the list of arguments.  
- You can assume all arguments can be converted to integer  
- If no argument passed, print 0  
- If the number of arguments is 1, print 0   
- You must use console.log(...) to print all output  
- You are not allowed to use var  

12. Object:  
mandatory  
Update this script to replace the value 12 with 89:  
- You are not allowed to use var  

12-object.js  
#!/usr/bin/node  
const myObject = {  
  type: 'object',  
  value: 12  
};  
console.log(myObject);  
/*  
YOUR CODE HERE  
*/  
console.log(myObject);  

13. Add file:  
mandatory  
Write a function that returns the addition of 2 integers.  
- The function must be visible from outside  
- The name of the function must be add  
- You are not allowed to use var  
Tip (https://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)   

14. Const or not const:  
#advanced  
Write a file that modifies the value of myVar to 333  

100-main.js  
#!/usr/bin/node  
myVar = 89;  
require('./100-let_me_const')  
console.log(myVar);  

Hint: Scope  
This exercise doesn’t pass semistandard so don’t worry about it.  

15. Call me Moby:  
#advanced  
Write a function that executes x times a function.  
- The function must be visible from outside  
- Prototype: function (x, theFunction)  
- You are not allowed to use var  

guillaume@ubuntu:~/0x12$ cat 101-main.js  
#!/usr/bin/node  
const callMeMoby = require('./101-call_me_moby').callMeMoby;  
callMeMoby(3, function () {  
  console.log('C is fun');  
});  
guillaume@ubuntu:~/0x12$ ./101-main.js  
C is fun  
C is fun  
C is fun  
guillaume@ubuntu:~/0x12$  

16. Add me maybe:  
#advanced  
Write a function that increments and calls a function.  
- The function must be visible from outside  
- Prototype: function (number, theFunction)  
- You are not allowed to use var  

guillaume@ubuntu:~/0x12$ cat 102-main.js  
#!/usr/bin/node  
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;  
addMeMaybe(4, function (nb) {  
  console.log('New value: ' + nb);  
});  
guillaume@ubuntu:~/0x12$ ./102-main.js  
New value: 5  
guillaume@ubuntu:~/0x12$  

17. Increment object:  
#advanced  
Update this script by adding a new function incr that increments the integer value.  
- You are not allowed to use var  

guillaume@ubuntu:~/0x12$ cat 103-object_fct.js  
#!/usr/bin/node  
const myObject = {  
  type: 'object',  
  value: 12  
};  
console.log(myObject);  
/*  
YOUR CODE HERE  
*/  
myObject.incr();  
console.log(myObject);  
myObject.incr();  
console.log(myObject);  
myObject.incr();  
console.log(myObject);  

guillaume@ubuntu:~/0x12$ ./103-object_fct.js  
{ type: 'object', value: 12 }  
{ type: 'object', value: 13, incr: [Function] }  
{ type: 'object', value: 14, incr: [Function] }  
{ type: 'object', value: 15, incr: [Function] }  
guillaume@ubuntu:~/0x12$  
