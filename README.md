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

#### Question 25:
Define a class, which have a class parameter and have a same instance parameter.<br/>
