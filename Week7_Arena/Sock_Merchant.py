n = int(input())
ar = list(map(int, input().split()))
result = 0
for i in range(min(ar), max(ar)+1):
    result += ar.count(i) // 2
    while ar.count(i) > 0:
        ar.remove(i)
print(result)