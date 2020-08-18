N = ' '.join(input()).split()
int_list = list(map(int, input().split()))
print(all(int_list[i] > 0 for i in range(len(int_list))) and N == N[::-1])