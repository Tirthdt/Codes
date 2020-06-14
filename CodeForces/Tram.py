n = int(input())

exiting, arrivals = [[], []]

for i in range(n):
    a, b = map(int, input().split())
    exiting.append(a)
    arrivals.append(b)

maximum_capacity = [arrivals[0]]

for i in range(n-1):
    maximum_capacity.append(maximum_capacity[i] - exiting[i+1] + arrivals[i+1])

print(max(maximum_capacity))
