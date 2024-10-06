#name: Feifan Yang

#pe6_1, E:
a, b, c = 2, 3, 0
print((a == b) and ((a * a < b * b) or (b < a) and (2 * a < b)))
# answer: false


#pe6_6, C,D:

#C
'''
major = "Computer Science"
if major == "Engineering Technology" Or "Computer Technology")
    print("Yes")
'''

major = "Computer Science"
if major == "Engineering Technology" or major=="Computer Technology":  #'or' and ':' at the end. 
    print("Yes")                      # ^^^^^ 'or' is sparate to two condition.


#D

'''
a, b = 1, 1.0
if a = b:
    print("same")
'''
a, b = 1, 1.0
if a == b:
    #^^ missing a '='
    print("same")

