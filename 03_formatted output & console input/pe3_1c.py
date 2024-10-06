n=1234
print(type(n))
print("01234567890123456789")
print(f"{n:10}{n:^10}"+"a")
'''
        {n:} is let the last integer of n at no.10.
        {n:^10} is make the integer n at the middle of 10 space,
        so the length of n is 4, the left and right space is (10-4)/2=3.
'''
print("01234567890123456789")
print(f"{n:<10}{n:>10}")
'''
        the < and > at here is make the integer left alignment and right alignment.
        the number 10 is mean the totale place for n is 10 place.
'''
print("01234567890123456789")
print(f"{n:10.3f}{n:10,.2f}{n}")
'''
        {n:10.3f} is same like {n:10}, but will shift to left 4 place,
        because the "." is take a space and 3 place of the floating point.
        {n:10,.2f} is a "," in between it's adding "," every thousand.
'''
print("012345678901234567890123456789")
print(f"{n:10.2%}{n:12,.2%}")
'''
        {n:10.2%} base on {n:10.3f} adding the "%" at the end, and 2 place of decimal.
        {n:12,.2%} base on {n:10,.2f} adding the "%" at the end, and 2 place of decimal.
'''
