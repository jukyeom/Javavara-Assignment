number = int(input("숫자를 입력하세요 "))
if number % 2 == 1:
    print("Weird")
else :
    if 2 <= number <= 5:
        print("Not Weird")
    elif 6 <= number <= 20:
        print("Weird")
    else :
        print("Not Weird")
        