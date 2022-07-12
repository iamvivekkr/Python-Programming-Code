#WHILE LOOP, BREAK & CONTINUE

i=0
while(i<10):
    print(i)
    i=i+1


#BREAK

i=0
while(True):
    print(i)
    if(i==4):
        break
    i=i+1

#CONTINUE

i=0
while(True):
    if i+1<3:
        i=i+1
        continue
    print(i+1)
    if(i==4):
        break
    i=i+1