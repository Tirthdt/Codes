for _ in range(int(input())):
    ts = int(input())
    while ts % 2 != 1:
        ts = ts // 2
    print(ts//2)
