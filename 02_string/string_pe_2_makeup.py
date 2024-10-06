#Name: Feifan Yang
# QUESTION: 1-5

# QUESTION: 1
namechar='''
* * * * *      * *         *
*            *     *
* * * *     * * * * *      *
*            *             *
*              * * *       *
'''
print(namechar)

## QUESTION: 2
count,star = 0,1
triangle = int(input("how many level is the triangle ?\n"))
print()
while triangle>count:   # "while" is a function use for the code run in certain conditions.
    print(' '*((triangle-1)-count)+'*'*star+'\n')
    count+=1 #count how many level is now.
    star+=2  #every level the star will have 2 more.

## QUESTION: 3
greet='welcome to a new semester!'
print(greet.capitalize())
first,last='feifan','yang'
name=first+' '+last
print('Name: '+name.title())
class1,class2,class3='et506','et704','et575'
courses=class1+'\t'+class2+'\t'+class3
print('Courses: '+courses.upper())
print('\n\n')

## QUESTION: 4
email='feifan.yang86@qcc.cuny.edu'
print('Email address: '+email[:])
print('User name: '+email[:(email.find('@'))].lower())
print('Company name: '+email[email.find('@')+1:email.rindex('.')].upper())

## QUESTION: 5_a
interest = 0.05         # '=' is assign symbols
balance = 10            #assign the right value to the left
print(interest*balance)

## QUESTION: 5_b
"""
bal = 123        #integer
dep = $100,000   #string
print(bal+dep)   #they can't have operation
"""
bal = 123
dep = 100000
print("$"+"{0:6,d}".format(bal+dep),end="")

## QUESTION: 5_c
'''
a = 2
b = 3
a+b = c #the variable want to be assign value should on left.
print(c)
'''
a = 2
b = 3
c=a+b
print(c)

## QUESTION: 5_d
'''
txt = "Hi"
class = 574     #"class" can't be a variable name.
print(txt+class)#integer can't concatenation with string.
'''
txt = "Hi"
Class = "574"
print(txt+Class)

## QUESTION: 5_e
'''
n = 1234
print(n[0]) #index only for string.
'''
n = "1234"
print(n[0])

## QUESTION: 5_f
'''
phoneNum = 718-631-6262         #make it be a string is the best way.
print('QCC phone number is '    #because we have to concatenation.
+ phoneNum)
'''
phoneNum = '718-631-6262'
print("QCC phone number is "
+ phoneNum)
