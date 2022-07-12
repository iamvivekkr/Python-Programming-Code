#IF ELSE & ELIF
var1=4
var2=53
var3=int(input("Enter any value: "))
if var3>var2:
    print("Greater")
elif var3==var2:
    print("Eual")
else:
    print("Lesser")


#in keyword
list=[1, 2, 3, 4]
print(2 in list)  #print true  or false
if 2 in list:
    print("Yes it is in the list")

#not in keyword
list=[1, 2, 3, 4]
print(5 not in list)  #print true  or false
if 5 not in list:
    print("Yes it is not in the list")