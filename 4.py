#STRING SLICING AND OTHER FUNCTIONS

mystr = "vivek is a good boy"
print(mystr)
print(mystr[2])
print(mystr[0:5]) #print till vivek
print(mystr[0:]) #print all
print(mystr[:5]) #print till vivek
print(mystr[:]) #print all
print(mystr[0:5:2]) #print till vivek and escape 1 char
print(mystr[0:5:3]) #print till vivek and escape 2 char
print(mystr[::]) #it means[0:19:1] print all
print(mystr[-4:]) #count from end
print(mystr[-4:-1]) #print from end 4 char and escapee 1 char
print(mystr[::-1]) #print opposite all
print(mystr[::-2]) #print opposite nd escape 1 char
print(type(mystr))

#some function

print(mystr.isalnum())
print(mystr.endswith("boy")) #check at last boy is there or not
print(mystr.count("v")) #print how much type u have type v in the string
print(mystr.capitalize()) #caapital letter only first char
print(mystr.find("is")) #print index of "is" is:-
print(mystr.lower()) #print all in small letter
print(mystr.upper()) #print all  in capital letter
print(mystr.replace("is", "are"))