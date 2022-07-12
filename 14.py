#FILE IO BASICS

"""
   "r" = open file for reading(default mode)
   "w" = open a file for writing
   "x" = creates file if not exists
   "a" = add more content to a file
   "t" = text mode(default)
   "b" = binary mode
   "+" = read &write
"""

#FOR READING :-
#(name)(tags)
f = open("vivek.txt")
#   OR
# f=open("vivek.txt", "r")
content = f.read()
print(content)
f.close()

#..............OR.......
f=open("vivek.txt", "rt")
for line in f:
   print(line, end="")

#Readline function
f=open("vivek.txt", "rt")
print(f.readline()) #print first line
print(f.readline()) #print ssecond line

#Readlines function
f=open("vivek.txt", "rt")
print(f.readlines()) #print all line

#FOR WRITING
f=open("vivek.txt", "w")
a=f.write("wow vivek") #delete and add this line
f.close()

#.............
f=open("vivek.txt", "a")
a=f.write("wow vivek") #print number of words
print(a)
f.close()

#FOR READ AND WRITE MODE

f==open("vivek.txt", "rt")
print(f.read()) #for return content
f.write("thank u") #for add line


