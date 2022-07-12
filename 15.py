# SEEK(), TELL() AND MORE ON PYTHON FILES

f=open("vivek2.txt")
print(f.tell())  #print position of the index
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.close()

#...........seek()
f=open("vivek2.txt")
print(f.readline())
print(f.seek(0)) #print once again same upper line seek(0)= 0th position se start
print(f.readline())
f.close()