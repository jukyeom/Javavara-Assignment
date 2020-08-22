N, M = map(int, input().split())
athlete = []
for _ in range(N):
    athlete.append(list(map(int, input().split())))
athlete.sort(key = lambda attribute : attribute[int(input())])
for i in range(len(athlete)):
    print(" ".join(athlete[i]), end = ' ')