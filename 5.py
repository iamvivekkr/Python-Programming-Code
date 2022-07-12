#PYTHON LISTS AND LIST FUNCTIONS and TOPPLE

grocery = ["paste", "vim", "toffee", "deorant"]
print(grocery[3])
numbers = [2, 3, 4, 5, 6]
print(numbers[2])
print(min(numbers))
print(max(numbers))



#Functions

numbers.sort() #function for increasing order
print(numbers)

numbers.reverse() #function for print opposite
print(numbers)

numbers.append(8) #function for add number
print(numbers)

numbers.insert(2, 1) #function for change number through index
print(numbers)

numbers.remove(8) #function for particular number
print(numbers)

numbers.pop() #function for remove last number
print(numbers)

numbers[2] = 52 #another function for change number through index
print(numbers)

#Mutual - can change [list]
#Immutual - cannot change (TOPPLE)

tp = (1, 2, 3)
print(tp)
#tp[1]=8 , show error becz its a topple therefore we cant change

#swap two numbers from python

a=2
b=3
a,b = b,a
print(a, b)