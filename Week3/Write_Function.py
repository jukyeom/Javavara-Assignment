def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
year = int(input("What year is this year? "))
print(is_leap(year))

# HackerRank에서는 작동되는데 VS Code에서는 작동을 안함.