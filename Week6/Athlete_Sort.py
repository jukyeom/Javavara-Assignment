N, M = map(int, input().split())
athlete = []
for _ in range(N):
    athlete.append(list(map(int, input().split())))
for i in range(len(athlete)):
    athlete.sort(key = lambda attribute : attribute[int(input())])
    print(" ".join(athlete[i]), end = '')