num = int(input("Enter a number: "))
BIT = 8
list=[0,0,0,0,0,0,0,0]
for BIT in range (7):
    count=7-BIT
    if (num>=2**count):
            num-=2**count
            list[BIT]=1
print (list)
for BIT in range (8):
      if (list[BIT]==1):
            list[BIT]=0
      else:
            list[BIT]=1
for BIT in range (8):
      if (list[7-BIT]==1):
            list[7-BIT]=0
      else:
            list[7-BIT]=1
            break
print(list)