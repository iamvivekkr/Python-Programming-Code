#OPERATORS
#...........Arithmertic.............

print("5+6 is", 5+6)
print("5-6 is", 5-6)
print("5*6 is", 5*6)
print("5/6 is", 5/6)
print("5**6 is", 5**6)    #5^6
print("5%6 is", 5%6)      #remainder value comes

#..........Assignment..............

x=5
print(x)
x+=7     #x+7
print(x)
x/=7     #x/7
x-=7     #x-7
x%=7     #x%7

#...........Comparision...........

i=8
print(i==5)
print(i!=5)
print(i>5)
print(i<5)
print(i>=5)
print(i<=5)

#...........Logical..............

a=True
b=False
print(a and a)     # T
print(a and b)     # F
print(a or a)      # F
print(a or a)      # T
print(a is a)      # F
print(a is not a)  # T
print(5 is not 7)  # T
print(5 is not 5)  # F

#............Membership.........

list = [3,3,2,2,33,45,35]
print(33 in list)
print(323 in list)
print(353 not in list)

#............Bitwise............

print(0 & 1)     #[0]
print(0 | 1)     #[1]
print(0 | 3)     #[3]
print(0 & 2)     #[0]