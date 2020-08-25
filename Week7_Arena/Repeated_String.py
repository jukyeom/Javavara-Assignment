s = input()
n = int(input())
my_str = s * (n // len(s)) + s[:n % len(s)]
print(my_str.count('a'))