a,b,c='Python','C++','Java'
newvar='Python'+' '+'C++'+' '+'Java'
#print(a+"\n",b,"\n",c,'\n',newvar)
print(a,'\n'+b,'\n'+c,'\n'+newvar)

var='apple '
print(var.capitalize()*3)

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
