#USING WITH BLOCK TO OPEN PYTHON FILES

with open("vivek3.txt") as f:
    a=f.read(4)
    print(a)     #here no need to close file becz we use with