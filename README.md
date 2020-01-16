# Coding Challenges 
### 100 code challenges in Python 
#### I commit to trying to solve at least one per day :v: <br/><br/>

#### Question 1: 
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
<br/>[Answer](c_1.py)

#### Question 2:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.  
Suppose the following input is supplied to the program:  
8  
Then, the output should be:  
40320
<br/>[Answer a) with a recursive function](c_2a.py)
<br/>[Answer b) with loop](c_2b.py)

#### Question 3:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.  
Suppose the following input is supplied to the program:  
8 . 
Then, the output should be:  
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
<br/>[Answer](c_3.py)

#### Question 4:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.  
Suppose the following input is supplied to the program:  
34,67,55,33,12,98   
Then, the output should be:  
['34', '67', '55', '33', '12', '98']  
('34', '67', '55', '33', '12', '98')
<br/>[Answer](c_4.py)

#### Question 5:
Define a class which has at least two methods:  
getString: to get a string from console input  
printString: to print the string in upper case.  
Also please include simple test function to test the class methods.
<br/>[Answer](c_5.py)

#### Question 6:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.  
Example
Let us assume the following comma separated input sequence is given to the program:  
100,150,180  
The output of the program should be:  
18,22,24
<br/>[Answer](c_6.py)

#### Question 7:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.  
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example  
Suppose the following inputs are given to the program:  
3,5  
Then, the output of the program should be:  
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
<br/>[Answer](c_7.py)

#### Question 8:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.  
Suppose the following input is supplied to the program:<br/>
without,hello,bag,world<br/>
Then, the output should be:<br/>
bag,hello,without,world
<br/>[Answer](c_8.py)

#### Question 9:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.  
Suppose the following input is supplied to the program:<br/>
Hello world<br/>
Practice makes perfect<br/>
Then, the output should be:<br/>
HELLO WORLD<br/>
PRACTICE MAKES PERFECT
<br/>[Answer](c_9.py)

#### Question 10:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.<br/>
Suppose the following input is supplied to the program:<br/>
hello world and practice makes perfect and hello world again<br/>
Then, the output should be:<br/>
again and hello makes perfect practice world
<br/>[Answer](c__10.py)

#### Question 11:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.<br/>
Example:<br/>
0100,0011,1010,1001<br/>
Then the output should be:<br/>
1010 <br/>
[Answer](c__11.py)

#### Question 12:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.<br/>
The numbers obtained should be printed in a comma-separated sequence on a single line.<br/>
[Answer](c__12.py)

#### Question 13:
Write a program that accepts a sentence and calculate the number of letters and digits.<br/>
Suppose the following input is supplied to the program:<br/>
hello world! 123<br/>
Then, the output should be:<br/>
LETTERS 10 <br/>
DIGITS 3 <br/>
[Answer](c__13.py)

#### Question 14:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. <br/>
Suppose the following input is supplied to the program: <br/>
Hello world! <br/>
Then, the output should be: <br/>
UPPER CASE 1 <br/>
LOWER CASE 9 <br/>
[Answer](c__14.py)

#### Question 15:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. <br/>
Suppose the following input is supplied to the program: <br/>
9 <br/>
Then, the output should be: <br/>
11106 <br/>
[Answer](c__15.py)

#### Question 16:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. <br/>
Suppose the following input is supplied to the program: <br/>
1,2,3,4,5,6,7,8,9 <br/>
Then, the output should be: <br/>
1,3,5,7,9 <br/>
[Answer](c__16.py)

#### Question 17:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: <br/>
D 100 <br/>
W 200 <br/>
D means deposit while W means withdrawal. <br/>
Suppose the following input is supplied to the program: <br/>
D 300 <br/>
D 300 <br/>
W 200 <br/>
D 100 <br/>
Then, the output should be: <br/>
500 <br/>
[Answer](c__17.py)

#### Question 18:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users. <br/>
Following are the criteria for checking the password: <br/>
1. At least 1 letter between [a-z] <br/>
2. At least 1 number between [0-9] <br/>
1. At least 1 letter between [A-Z] <br/>
3. At least 1 character from [$#@] <br/>
4. Minimum length of transaction password: 6 <br/>
5. Maximum length of transaction password: 12 <br/>
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma. <br/>
Example <br/>
If the following passwords are given as input to the program: <br/>
ABd1234@1,a F1#,2w3E*,2We3345 <br/>
Then, the output of the program should be: <br/>
ABd1234@1 <br/>
[Answer](c__18.py)

#### Question 19:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is: <br/>
1: Sort based on name; <br/>
2: Then sort based on age; <br/>
3: Then sort by score. <br/>
The priority is that name > age > score. <br/>
If the following tuples are given as input to the program: <br/>
Tom,19,80 <br/>
John,20,90 <br/>
Jony,17,91 <br/>
Jony,17,93 <br/>
Json,21,85 <br/>
Then, the output of the program should be: <br/>
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')] <br/>
[Answer](c__19.py)

#### Question 20:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n. <br/>
[Answer](c__20.py)

#### Question 21:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. <br/> The trace of robot movement is shown as the following: <br/>
UP 5 <br/>
DOWN 3 <br/>
LEFT 3 <br/>
RIGHT 2 <br/>
distance i <br/>
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.<br/>
Example: <br/>
If the following tuples are given as input to the program: <br/>
UP 5 <br/>
DOWN 3 <br/>
LEFT 3 <br/>
RIGHT 2 <br/>
Then, the output of the program should be: <br/>
2 <br/>
[Answer](c__21.py)

#### Question 22:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program: <br/>
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3. <br/>
Then, the output should be: <br/>
2:2 <br/>
3.:1 <br/>
3?:1 <br/>
New:1 <br/>
Python:5 <br/>
Read:1 <br/>
and:1 <br/>
between:1 <br/>
choosing:1 <br/>
or:2 <br/>
to:1 <br/>
[Answer](c__22.py)

#### Question 23:
Write a method which can calculate square value of number, using the ** operator <br/>
[Answer](c__23.py)

#### Question 24:
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.<br/>
Please write a program to print some Python built-in functions documents, such as abs(), int(), input() and add document for your own 
function. <br/>
[Answer](c__24.py)

#### Question 25:
Define a class, which have a class parameter and have a same instance parameter.<br/>
[Answer](c__25.py)

#### Question 26:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.<br/>
[Answer](c__26.py)

#### Question 27:
Define a function that can convert a integer into a string and print it in console.<br/>
[Answer](c__27.py)

#### Question 28:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.<br/>
[Answer](c__28.py)

#### Question 29:
Define a function that can accept two strings as input and concatenate them and then print it in console.<br/>
[Answer](c__29.py)

#### Question 30:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.<br/>
[Answer](c__30.py)

#### Question 31:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".<br/>
[Answer](c__31.py)

#### Question 32:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.<br/>
[Answer](c__32.py)

#### Question 33:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.<br/>
[Answer](c__33.py)

#### Question 34:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.<br/>
[Answer](c__34.py)

#### Question 35:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.<br/>
[Answer](c__35.py)

#### Question 36:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).<br/>
[Answer](c__36.py)

#### Question 37:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.<br/>
[Answer](c__37.py)

#### Question 38:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.<br/>
[Answer](c__38.py)

#### Question 39:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.<br/>
[Answer](c__39.py)

#### Question 40:
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
[Answer](c__40.py)

#### Question 41:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. <br/>
[Answer](c__41.py)

#### Question 42:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). <br/>
[Answer](c__42.py)

#### Question 43:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
[Answer](c__43.py)

#### Question 44:
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].<br/>
[Answer](c__44.py)

#### Question 45:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].<br/>
[Answer](c__45.py)

#### Question 46:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].<br/>
[Answer](c__46.py)

#### Question 47:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).<br/>
[Answer](c__47.py)

#### Question 48:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).<br/>
[Answer](c__48.py)

#### Question 49:
Define a class named American which has a static method called printNationality.<br/>
[Answer](c__49.py)

#### Question 50:
Define a class named American and its subclass NewYorker.<br/>
[Answer](c__50.py)

#### Question 51:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. <br/>
[Answer](c__51.py)

#### Question 52:
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. <br/>
[Answer](c__52.py)

#### Question 53:
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.<br/>
[Answer](c__53.py)

#### Question 54:
Please raise a RuntimeError exception.<br/>
[Answer](c__54.py)

#### Question 55:
Write a function to compute 5/0 and use try/except to catch the exceptions.<br/>
[Answer](c__55.py)

#### Question 56:
Define a custom exception class which takes a string message as attribute. Hints: To define a custom exception, we need to define a class inherited from Exception.<br/>
[Answer](c__56.py)

#### Question 57:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.<br/>

Example: If the following email address is given as input to the program: john@google.com <br/>

Then, the output of the program should be: john <br/>

In case of input data being supplied to the question, it should be assumed to be a console input. <br/>

Hints: Use \w to match letters.<br/>

[Answer](c__57.py)

#### Question 58:

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.<br/>

Example: If the following email address is given as input to the program: john@google.com <br/>

Then, the output of the program should be: google <br/>

In case of input data being supplied to the question, it should be assumed to be a console input. <br/>

Hints: Use \w to match letters.<br/>

[Answer](c__58.py)


#### Question 59:
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.<br/>
Example: If the following words is given as input to the program:<br/>
2 cats and 3 dogs.<br/>
Then, the output of the program should be:<br/>
['2', '3']<br/>
In case of input data being supplied to the question, it should be assumed to be a console input.<br/>
Hints:<br/>
Use re.findall() to find all substring using regex.<br/>
[Answer](c__59.py)

#### Question 60:
Print a unicode string "hello world".<br/>
Hints:<br/>
Use u'strings' format to define unicode string.<br/>
[Answer](c__60.py)

#### Question 61:
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.<br/>
Hints:<br/>
Use unicode() function to convert.<br/>
[Answer](c__61.py)

#### Question 62:
Write a special comment to indicate a Python source code file is in unicode.<br/>
[Answer](c__62.py)

#### Question 63:
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).<br/>
Example: If the following n is given as input to the program:<br/>
5<br/>
Then, the output of the program should be:<br/>
3.55<br/>
In case of input data being supplied to the question, it should be assumed to be a console input.<br/>
Hints:<br/>
Use float() to convert an integer to a float<br/>
[Answer](c__63.py)

#### Question 64:
Write a program to compute:<br/>
f(n)=f(n-1)+100 when n&gt;0<br/>
and f(0)=1<br/>
with a given n input by console (n&gt;0).<br/>
Example: If the following n is given as input to the program:<br/>
5<br/>
Then, the output of the program should be:<br/>
500<br/>
In case of input data being supplied to the question, it should be assumed to be a console input.<br/>
Hints:We can define recursive function in Python.<br/>
[Answer](c__64.py)

#### Question 65:
The Fibonacci Sequence is computed based on the following formula:<br/>
f(n)=0 if n=0<br/>
f(n)=1 if n=1<br/>
f(n)=f(n-1)+f(n-2) if n&gt;1<br/>
Please write a program to compute the value of f(n) with a given n input by console.<br/>
Example:<br/>
If the following n is given as input to the program:<br/>
7<br/>
Then, the output of the program should be:<br/>
13<br/>
In case of input data being supplied to the question, it should be assumed to be a console input.<br/>
Hints:<br/>
We can define recursive function in Python.<br/>
[Answer](c__65.py)

#### Question 66:
The Fibonacci Sequence is computed based on the following formula:<br/>
f(n)=0 if n=0<br/>
f(n)=1 if n=1<br/>
f(n)=f(n-1)+f(n-2) if n&gt;1<br/>
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.<br/>
Example:<br/>
If the following n is given as input to the program:<br/>
7<br/>
Then, the output of the program should be:<br/>
0,1,1,2,3,5,8,13<br/>
Hints:<br/>
We can define recursive function in Python.<br/>
Use list comprehension to generate a list from an existing list.<br/>
Use string.join() to join a list of strings.<br/>
In case of input data being supplied to the question, it should be assumed to be a console input.<br/>
[Answer](c__66.py)

#### Question 67:
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.<br/>
Example:<br/>
If the following n is given as input to the program:<br/>
10<br/>
Then, the output of the program should be:<br/>
0,2,4,6,8,10<br/>
Hints:<br/>
Use yield to produce the next value in generator.<br/>
In case of input data being supplied to the question, it should be assumed to be a console input.<br/>
[Answer](c__67.py)

#### Question 68:
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.<br/>
Example:<br/>
If the following n is given as input to the program:<br/>
100<br/>
Then, the output of the program should be:<br/>
0,35,70<br/>
Hints:<br/>
Use yield to produce the next value in generator.<br/>
In case of input data being supplied to the question, it should be assumed to be a console input.<br/>
[Answer](c__68.py)

#### Question 69:
Please write assert statements to verify that every number in the list [2,4,6,8] is even.<br/>
Hints:<br/>
Use "assert expression" to make assertion.<br/>
[Answer](c__69.py)

#### Question 70:
Please write a program which accepts basic mathematic expression from console and print the evaluation result.<br/>
Example:<br/>
If the following string is given as input to the program:<br/>
35+3<br/>
Then, the output of the program should be:<br/>
38<br/>
Hints:<br/>
Use eval() to evaluate an expression.<br/>
[Answer](c__70.py)

#### Question 71:
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.<br/>
Hints:<br/>
Use if/elif to deal with conditions.<br/>
[Answer](c__71.py)

#### Question 72:
Please write program to remove duplicates from two lists
[Answer](c__72.py)

#### Question 73:
Please generate a random float where the value is between 10 and 100 using Python math module.<br/>
Hints:<br/>
Use random.random() to generate a random float in [0,1].<br/>
[Answer](c__73.py)

#### Question 74:
Please generate a random int where the value is between 5 and 95 using Python math module.<br/>
[Answer](c__74.py)

#### Question 75:
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.<br/>
Hints:<br/>
Use random.choice() to generate a random element from a list.<br/>
[Answer](c__75.py)

#### Question 76:
Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.<br/>
Hints:<br/>
Use random.choice() to generate a random element from a list.<br/>
[Answer](c__76.py)

#### Question 77:
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.<br/>
Hints:<br/>
Use random.sample() to generate a list of random values.<br/>
[Answer](c__77.py)

#### Question 78:

[Answer](c__78.py)

#### Question 79:
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.<br/>
Hints:<br/>
Use random.sample() to generate a list of random values.<br/>
[Answer](c__79.py)

#### Question 80:
Please write a program to randomly print a integer number between 7 and 15 inclusive.<br/>
Hints:<br/>
Use random.randrange() to a random integer in a given range.<br/>
[Answer](c__80.py)







