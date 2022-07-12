#FOR LOOP
list1 = ["vivek", "saniya", "sanvi", "abhi"]
for item in list1:
    print(item)

         #OR

list1 = [["vivek",1] ["saniya",2] ["sanvi",3] ["abhi",4]]
for item, toffee in list1:
    print(item, toffee)


         #OR

list1 = [["vivek",1] ["saniya",2] ["sanvi",3] ["abhi",4]]
dict1 = dict(list1)
for item, toffee in dict1.items():       #dict items function use
    print(item, toffee)