#FUNCTION  & DOCSTRING

#...........Build in function........

a=9
b=8
c=sum((a, b))
print(c)         # 9+8=17

#User define function.................

def function1():

    print("Its user define func")
  #ita a wrong way       print(function1())
function1()   #to print


#.......................
def function(a, b):
       print("Its user define func", a+b)
function(5, 7)

#................................
def function2(a, b):
     average=(a+b)/2
     print(average)
     function2(5, 7)

#................

def function2(a, b):
    average=(a+b)/2
    return average
v=function2(5, 7)
print(v)


#...........................DOCSTRING............
#"""........"""
#print(function1()._doc_) #to print comment
