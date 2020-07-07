my_str = input("Write String ")
my_int, my_alpha = input("Write int and alphabet ").split()
my_int = int(my_int)
if my_int >= len(my_str):
    print("The number you gave is too large!")
else:
    replace_str = my_str[my_int].replace(my_str[my_int],my_alpha)
    new_str = my_str[:my_int] + replace_str + my_str[my_int+1:]
    print(new_str)

# 성공하긴 했지만 코드가 조금 복잡함.