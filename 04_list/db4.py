#name: feifan yang
#pe4 questions 1,6,7

#pe4_1.C
'''
strNum = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9" 
print(strNum[1], strNum[-1], len(strNum))   #second character,last character, lenght of this string.
print(strNum[:len(strNum)])                 #from start to then end of string(everything).
print(strNum[1]+strNum[-3])                 #second index, the thire index count it form the right.
'''
#pe4_6.C
'''
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n[0], n[9] = "apple", 'cherry'              #change the first index, which is '1' in the list to "apple",
                                            #change the 9 which is the last index '10' to cherry.


n.insert(3, "banana")                       #insert "banana" to index 3 which is the position of the '4' in the list,
                                            #after the insert movement "banana" will between '3' and '4' than the lenght
                                            #of this list will add 1.
    n.insert(-1, "kiwi")                    #insert "kiwi" to the last index which is position between '9' and '10' 
                                            #so the '10' will move one unit to the right, also add 1 to the lenght.
print(n)
print(f"Do you like {n[0].upper()} or {n[-1].upper()}?") #change first and last index write as capital.
'''

#pe4_7.C

#bug:
'''
word = 'sea'    
word[0] = 'p'   # i think here is want the first index of string change to 'p'
                #but string can't change like this.
print(word)
'''
#fixed:
'''
word = 'sea'
print('p'+word[1:]) # here is using the substring to cut the fist character than add the 'p' in the front.
'''




#immutable:
'''
str1='sdasdada'
print(id(str1))
str1='hdhfkdjshkjfs'
print(id(str1))
'''