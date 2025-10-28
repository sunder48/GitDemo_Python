for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

for i in range(7,1,-1):
    for j in range(1,i+1,):
        print(i,end=' ')
    print()

num=7
for i in range(num,0,-1):
    print('*'* i)

#Pyramid pattern
row=5
for i in range(1,row+1): # Handle the number of rows
    for j in range(row-i): # Hanlde the number of space
        print(" ",end="")
    for k in range(2*i -1): # Number of stars
        print('*',end="")
    print()

rows = 3
# Upper part
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
# Lower part
for i in range(rows - 2, -1, -1):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

