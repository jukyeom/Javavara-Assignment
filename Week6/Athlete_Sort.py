N, M = map(int, input().split())
athlete = []
for _ in range(N):
    athlete.append(list(map(int, input().split())))
for i in range(len(athlete)):
    athlete.sort(key = int(athlete[i][int(input())]))
    print(athlete[i], end = ' ')