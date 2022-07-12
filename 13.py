#TRY EXCEPT EXCEPTION HANDLING

print("Enteer num1")
num1=input()
print("Enter num2")
num2=input()
try:
    print("The sum is", int(num1)+int(num2))
except Exception as e:
    print(e)
    print("print this line is very important")

    #use of try &except becz program error in 5th line fir bhi wo uss error ko likj k aage run kare program