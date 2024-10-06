#question1:
#1_b:
'''b = []
for i in range (5):
    b.append(i)
print(b)
'''
#1_c:
'''x = list(range(-10, 10))
print(x)
print(min(x), max(x), sum(x))'''
#1_d:
'''even_num = list(range(2, 11, 2))
print(even_num[0], even_num[-1])
'''
#1_e:
'''oddlist=list(range(1,10,2))
print(oddlist)'''

'''oddlist=[num for num in range(1,10,2)]
print(oddlist)'''
#1_f:
'''cubelist=[num**3 for num in range(1,11)]
for num in cubelist:
    print(num)'''

'''for item in range(1,11):
    print(item**3)'''
#1_g:
''''
cubelist=[num**3 for num in range(1,11)]
for num in cubelist:
    print(num, end= '|')
'''

#question2:

'''for x in range(0,100,2):
    print(x)
'''


'''evenlist=[values*2 for values in range(0,50)]
print(evenlist[:5])
print(evenlist[-5:])
sublist=[]
for num in evenlist:
    if (num >=20 and num <=30):
        sublist.append(num)
print(sublist)
for i in evenlist[evenlist.index(20):evenlist.index(30)+1]:
    print(i,end=' ')
'''

#question3:

'''
q3_1list=[num*4 for num in range(0,11)]
print(q3_1list)
q3_2list=[num//2 for num in q3_1list]
print(q3_2list)
q3_3list=[num//2 for num in q3_2list]
print(q3_3list)
'''


#question4:

'''
months = ['january', 'february', 'march', 'april', 'may', \
    'june', 'july', 'august', 'september', 'october', 'november', 'december']
print(f"Original list:\n{months}\n")
three_letter_list=[]
for item in months:
    three_letter_list.append(item[:3].upper())
print(f"Three-letter abbreviation 1-12:\n{'|'.join(three_letter_list)}\n\n\
New list:\n{three_letter_list}")
'''


#question 5:
'''
numrange=int(input("Enter a range: "))
integernumber=int(input("Enter a integer number: "))
rangelist=[item for item in range(1,numrange+1)]
print(f"Mulitipication Table of {numrange}")
for item in rangelist:
    print(f"{item}\t*\t{integernumber}\t=\t{item*integernumber}")
'''
a=2
b=3 
print(type(a+b)) 
print(type((a+b,))) 
print(type(()))
t=(a+b)
