#question_1:
'''
import math
denominator=0

while denominator==0:
    numerator=int(input("Enter a numerator: "))
    denominator=int(input("Enter a denominator: "))
    print("Denominator cannot be zero. Try again.\n")               ####problem
print(f"{numerator} mod {denominator} = {int(math.fmod(numerator,denominator))}")
'''

#question_2:
'''
from math import isqrt
from random import randint

num= randint(1,100)
num2=isqrt(num)
print(f"square root of {num} = {num2}")
'''
#feifan yang
#question_3:
'''
def hello():
    print("Hello World")
'''
#question_4:

'''
def HelloNo(n):
    for i in range(n):
        hello()

HelloNo(3)

'''
#question_5:
'''
import random
def massage(text,n):
    for i in range(n):
        print(text)

def main():
    text = input("Enter a text: ")
    n=random.randint(1,10)
    print(f"text = {text}\nn = {n}\nmessage(text, n) will print the following:")
    massage(text,n)

main()
'''

#question_6:
'''
def middle(l):
    l'''

#db2:
def f(x):
    if x >0: 
        return True
    return False
