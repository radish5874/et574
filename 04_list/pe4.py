#quesion_1a:
'''print("Python")     #whole string
print("Python"[0])  #first index
print("Python"[-1]) #last index
print("Python"[:])  #whole string '''
#quesion_1c:
'''strNum = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
print(strNum[1], strNum[-1], len(strNum))   #   ,"-1" last index
print(strNum[:len(strNum)])                 # "[0:to the end]"
print(strNum[1]+strNum[-3])'''

#question2:
'''n=[]                        #a
additem=('2','4')
n.extend(additem)           #b
print(n)                    #c
n.insert(0,'0')             #d
n.insert(1,'1')
n.insert(3,'3')
print(n)
n.insert(5,'5')             #f
print(n)
ritem=int(n.pop(0))         #h
print(n)
ritem1=int(n.pop(1))        #j
print(n)
print(ritem1)
ritem2=int(n.pop(2))        #l
print(n)
print(ritem2)
print("Sum of all removed number = ",ritem+ritem1+ritem2)  #n,m
n[0]=100
n[2]=9.9
print(n)
newNum= n.copy()            #p
n.clear()
print(f"Original list = {n}\nNew Lits = {newNum}")
del n
print(n)'''

#question3:
'''
courses=['dan111','et574','et575','et580','et585','et123']
print(courses)
print(f"I am taking {len(courses)} courses")
print(courses[0],courses[-1])
print(courses[0:4])
print(courses[-4:])
print(courses[1:-1])
'''

#question4:
'''grades=input("enter your grades splitting by ','")
grades=[int(i) for i in grades.split(',')]
print(sum(grades)/len(grades))
'''

#question5:
'''
fullname=input("enter your fulllname: \n").split(' ')
print(f"First Name: {fullname[0]}\nLast Name: {fullname[-1]}")
'''
