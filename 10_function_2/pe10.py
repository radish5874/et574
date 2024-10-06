#question_4:
'''
def printName(*names):
    for name in names:
        print(name,end=' ')
'''

#question_5:

'''
def main():
    user_1=createUser(name= 'John',
    age= '43',
    job='Programmer',
    hobby= 'Biking')
    printUser(user_1)

def createUser(name,age,**user_info):
    user_info['name']=name
    user_info['age']=age
    return user_info

def printUser(user):
    for k,v in user.items():
        print(k,v)

main()
'''
#question_6:

def average(*number):
    return(f'{number} : {sum(number)/len(number):.2f}')

def main():
    import random
    print(average(95,87,83,74))
    x=random.randint(-100,0)
    y=random.randint(0,2)
    z=random.randint(1,101)

    print(average(x,y,z))
