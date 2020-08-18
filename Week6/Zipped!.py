N, X = map(int, input().split())
score = []
for i in range(X):
    score.append(list(map(float, input().split())))
for student in list(zip(*score)):
    print(sum(student) / len(student))