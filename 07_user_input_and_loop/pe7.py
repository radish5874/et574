#question_1:

'''
userin=int(input("Enter an integer number, and I'll tell you if it's a multiple of ten: "))
while userin%10 !=0:
    userin=int(input("Enter an integer number, and I'll tell you if it's a multiple of ten: "))
print(f"{userin} is a multiple of ten.")
'''

#question_2:
'''
for num in range(1,1001):
   if num%2==0 and num%3==0:
    print(num, end=' ')
'''

#question_3_a:
'''
sum=0
for num in range(1,101):
    sum += num
print(sum)
'''

#question_3_b:
'''
sum=0
for num in range(1,101):
    if num%2==0:
        sum += num
print(sum)
'''
#question_4:

'''
userin= int(input("Enter a positive number: "))
if (userin <5 ):
    print("Invalid input.")
else:
    print(f"Range = 1 to {userin}")
    for num in range (1,userin+1):
        if (num%5==0 and num%2!=0):
            print(num,end=' ')
'''

#question_5:


'''
num=9
while(num>0):
    print(num)
    num=num-1
print("Happy New Year!")
'''

'''
num=9
for num in reversed(range(1,num+1)):
    print(num)
    num=num-1
print("Happy New Year!")
'''

#question_6:
'''
list_range=int(input("Enter the number of grades in the list: "))
import random

original_list=[]
for num in range(list_range):
    original_list.append(random.randint(1,100))


passing_grade=int(input("Enter the passing grade: "))


updated_list=[]
for num in original_list:
    if num > passing_grade:
        updated_list.append(num)
print(f"Updated List: {updated_list}")        
print(f"Original List: {original_list}")
'''

#question_7:

'''
numlist=[]
num=1.1
while num!=0:
    num=float(input("Enter a number or 0 to stop: "))
    if num==0:
        break
    numlist.append(num)

print(f"Sum = {sum(numlist)}\nAverage = {sum(numlist)/len(numlist)}\n\
Number(s) entered:")
for num in numlist:
    print(num,end=' ') ## not finish
'''
#question_8:
'''
n1=int(input("enter a number n1: "))
n2=int(input("enter a number n2: "))
if n1==n2:
    print("n1 = n2")
elif n1<n2:
    while n1!=n2+1:
        print(n1,end=':')
        n1+=1
else:
    for num in reversed(range(n2,n1+1)):
        print(num,end=':')
'''
#question_9:

'''
lower=int(input("Enter the lower bound: "))
upper=int(input("Enter the upper bound: "))
incval=int(input("Enter a number to increment: "))

print("USING WHILE LOOP")
temp=lower
while temp<upper:
    print(temp)
    temp+=incval
print(upper)

print("SUING FOR LOOP")
for num in range (lower,upper,incval):
        print(num)
print(upper)'''

