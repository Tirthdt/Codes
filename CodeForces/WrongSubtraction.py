n, no_of_sub = map(int, input().split())

for i in range(no_of_sub):
    if n % 10 != 0:
        n -= 1
    else:
        n = n//10
print(n)
