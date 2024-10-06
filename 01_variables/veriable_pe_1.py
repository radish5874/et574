#question_1
print("John\nSmith")
print("\n\n")
#question_2r
print("Item\t\tPrice\n\
Apple\t\t$1.75\n\
Banana\t\t$2.25\n\
Cherry\t\t$3.50\n\
--------\t-------\n\
Total\t\t$7.50")#because the line 9 need more than 2 indent,so in other line need 2 indent.
print("\n\n")
# question_3
print('Albert Einstein once said, \n\
"A person who never made a mistake\n\
never tried anything new."')#''is mean this is a string
print("\n\n")
#question_4
price, discountPercent= 99.99,25

markdown = discountPercent / 100 * price
finalprice = price - markdown
print(f'price={finalprice:.2f}')
print("price="'%.2f'%finalprice)
print("price=",round(finalprice,2))
print("\n\n")
#question_5
a=23456
b=23678
gallonuse=9
distancetraveled=b-a
answer=distancetraveled/gallonuse
print("Distance Traveled: ",distancetraveled," Miles\n\
Gallon Used: ",gallonuse,"Gallons\n\
How many miles per gallon did the \
car average between two fillings?\n\
Answer: ",round(answer,3),"Miles/Gallon")
print("\n\n")
#question_6_1-12
print(2+3*4)    # * 乘法 (Multiplication)
print(1-7**2)   # ** 次方 ("^"nth power)
print(1//2**3)  # // 左除右取整 (left divided by right, than only take the integer part)
print((3+4)*5)
print((5%3)*4)  # % 余数 (left divided by right, remainder)
print((-2)**(-2))# (-2)^(-2)
print(7//3)
print(14%4)
print(1+7%4)
print(14//4*4)
print(5//2+2)
print(5%5*5)
print("\n\n")
#13-18 the veriable name can't be:
        #1.no any symbols, except _ under line.
        #2.no space.
        #3.no number in front.
#19-24 rewrite the statements using augmented assignment operators.

    #增强赋值符号就是所有运算符在等号左边的简写运算符.
    #Example:=,+=,-=,*=,/=,%=,**=.(被赋值的变量同时也是被改变的变量。)
cost=sum=product=total=quotient=100#set default valume
rate=num=10#set default valume

cost+=5
print(cost)
sum*=rate
print(sum)
product/=10
print(product)
cost=100    #set default valume
cost//=num
cost=100    #set default valume
print(cost)
total-=cost
print(total)
quotient%=rate
print(quotient)
print("\n\n")
    #25-27 (a=5,b=2)
a=5
b=2
print(int(-a/b),"\t",round(a/b,2),"\t",abs(b-a))
