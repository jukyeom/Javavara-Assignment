n = int(input())
def fibonacci(n):
    if n == 0:
        fibo_list = []
    elif n == 1:
        fibo_list = [0]
    else:
        i = 0
        fibo_m = 0
        fibo_n = 1
        fibo_list = [fibo_m, fibo_n]
        while i < n:
            i += 1
            fibo_m = fibo_m + fibo_n
            fibo_n = fibo_n + fibo_m
            fibo_list.append(fibo_m)
            fibo_list.append(fibo_n)
            del fibo_list[n:]
    return fibo_list
cube = lambda i : i**3
print(list(map(cube, fibonacci(n))))