#question_2:
'''
age=int(input("Age = "))
if age<0:
    print("invalid age.")
elif age <2:
    print("you're a baby.")
elif age <4:
    print("you’re a toddler.")``
elif age <13:
    print("you’re a kid.")
elif age <20:
    print("you’re a teenager.")
elif age <65:
    print("you’re an adult.")
else:
    print("you’re an elder.")
'''

#question_3:

'''
username=['Tom','Jerry','Bob','Dora','ADMIN']
if len(username):
    for item in username:
        if item == 'ADMIN':
            print("Hello ADMIN, would you like to see a status report?")
        else:
            print(f"Hello {item}, thank you for logging in again!")
else:
    print('We need to find some users.')
'''

#question_4:
'''current_users=[ 'admin','tom','jerry','Dora','GEORGE']
username= input('Enter your user name: ')
for name in current_users:
    if username == name:
        print(f"Sorry {name}, that name is taken.")
print(current_users)'''



'''current_users=[ 'admin','tom','jerry','Dora','GEORGE']
username= input('Enter your user name: ')
if current_users.count(username):   #using the .count() to find is the username are in the list alrealy.
    print(f"Sorry {username}, that name is taken.\nCurrent users:{current_user}")
else:
    print(f"Great, {username} is still available.")
    current_users.append(username) 
print('Updated users: ',current_users)'''


#question_5:


'''
vehicles=['car','Truck','boat','PLANE']
search_letter=input('Enter a search letter: ').lower()
if (ord(search_letter)>=65 and ord(search_letter)<=90) or (ord(search_letter)>=97 and ord(search_letter)<=122):
    for item in vehicles:
        if (item.lower()).count(search_letter):
            print(f"{item} contains ‘{search_letter}’ and it is in position {(item.lower()).find(search_letter)}.")
        else:
            print(f"{item} does not contain ‘{search_letter}’.")
else: 
    print("Invalid search letter.")

'''