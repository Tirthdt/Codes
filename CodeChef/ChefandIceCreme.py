for _ in range(int(input())):
    n = int(input())
    customers = [int(x) for x in input().split()]
    currencies = {
        5: 0,
        10: 0,
        15: 0
    }
    if customers[0] != 5:
        print("NO")
    else:
        currencies[5] += 1
        for i in range(1, n):
            balance = customers[i] - 5
            if balance == 0:
                currencies[5] += 1
            elif balance == 10:
                if currencies[10] > 0:
                    currencies[10] -= 1
                    currencies[15] += 1
                elif currencies[5] >= 2:
                    currencies[5] -= 2
                    currencies[15] += 1
                else:
                    print("NO")
                    break
            elif balance == 5:
                if currencies[5] > 0:
                    currencies[5] -= 1
                    currencies[10] += 1
                else:
                    print("NO")
                    break
        else:
            print("YES")
