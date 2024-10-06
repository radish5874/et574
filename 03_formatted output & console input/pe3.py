#question:2
'''
bill =float(input("Enter the amount of the bill: "))
ptip =int(input("Enter the percentage of tip: "))
tip =bill * (ptip/100)
print(f"Tip: ${tip:.2f}")
'''
#question:3
'''
height=float(input("Please enter the height (in cm): "))
weight=float(input("Please enter the weight (in kg): "))
bmi=(weight/(height*height))*703
print(f"BMI = {bmi:.3f}")
'''
#question:4

'''
first=input("Please enter the first integer: ")
second=input("Please enter the second integer: ")
thire=input("Please enter the thire integer: ")
print(f"Before sorting {first} {second} {thire}")
nlist=[first,second,thire]
nlist.sort()
print(' '.join(nlist))
'''


''' not finish
first=input("Please enter the first integer: ")
second=input("Please enter the second integer: ")
thire=input("Please enter the thire integer: ")
x= min(first,second,thire)
print(x)
#print(min(first,second,thire),''.join(min),max(first,second,thire))
'''
#question_5

'''
word = input("enter any word: ")
count = len(word)
output =[]                          #set output be a list.
while count>0:                      #run when the word length large than 0.
    count-=1                    #-1 is because we have to dispaly the word
                                #reverse. And the reason why, i didnot put this
                                #in here, is because using the number of length for
                                #index will have a extra. so i have to -1 first.
    output.append(word[count])      # using the append to add the letter in to list.
print(''.join(output))              #'char'.join(listname)  this is a function is use
                                    #for the out put of list, we can change the intervals of the output
'''
