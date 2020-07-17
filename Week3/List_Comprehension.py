x = int(input("Type a number X "))
y = int(input("Type a number Y "))
z = int(input("Type a number Z "))
n = int(input("Type a number N "))
new_list = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) \
            for k in range(0,z+1) if i+j+k != n]
print(new_list)