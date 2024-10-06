#Name: Feifan Yang

#question_6:
'''
stuInfo_1={'name':'fei','gpa':1.23}
stuInfo_2={'name':'fan','gpa':2.34}
stuInfo_3={'name':'yang','gpa':3.56}
stuClass=[stuInfo_1,stuInfo_2,stuInfo_3]
print(f"All student in the list:\n{stuClass}")

student_number=1
print("\nAll student information:")
for i in stuClass:
    print(f"student {student_number} {i}")
    student_number+=1

print("\nAll gpa information:")
for i in stuClass:
    print(i['gpa'],end='|')

print("\n\nAll the update information:")
stuClass[-1]['gpa']=4.0 #'[-1]' last student,'[gpa]' find the keys.

for i in stuClass:
    print(f"{i['name']}\t\t{i['gpa']:.2f}")
'''
'''
#quesion_7a:

letter_list=[]
number_list=[]

for letter in range(97,123):
    letter_list.append(chr(letter))
print(letter_list)

for num in range(1,27):
    number_list.append(num)
print(number_list)

charNum=dict(zip(letter_list,number_list))

for i in charNum:
    print(f"{i}|{charNum[i]}",end=' ')
  

#question_7b:

letter_list=[]
number_list=[]

for letter in range(65,91):
    letter_list.append(chr(letter))
print(letter_list)          #

for num in range(100,2700,100):
    number_list.append(num)
print(number_list)          #

numChar=dict(zip(number_list,letter_list))

for i in numChar:
    print(f"{i} {numChar[i]}",end='|')

all={}
all.update(charNum)
all.update(numChar)
print("\\n\n\n\n\n",all)

'''