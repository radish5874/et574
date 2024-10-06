str1="Python"
print(len(str1))
print(str1[-5:5])
'''why the "[-100:10]" will have the "Python" out put,
   for this example "Python":
string:       P y t h o n
count:       0 1 2 3 4 5 6
   so when it is a negative number, than it will count from right to the left
   which is mean the lsat character is -1.
string:                                       | P| y| t| h| o| n|
count:                                        0  1  2  3  4  5  6  7  8  9  10  11
count by negative:                  -9 -8 -7 -6 -5 -4 -3 -2 -1  0

    if the first number is 0 or the negative number of the srting length;
    and second number is large than the string length, the output will have whole string.

'''
