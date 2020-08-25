n = int(input())
s = input()
sealvl = 0
result = 0
for i in s:
    if i == 'U':
        sealvl += 1
        if sealvl == 0 :
            result += 1
    else:
        sealvl -= 1
print(result)