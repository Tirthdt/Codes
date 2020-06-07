"""
There are N students standing in a row and numbered 1 through N from left to right. You are given a string S with length N, where for each valid i, the i-th character of S is 'x' if the i-th student is a girl or 'y' if this student is a boy. Students standing next to each other in the row are friends.

The students are asked to form pairs for a dance competition. Each pair must consist of a boy and a girl. Two students can only form a pair if they are friends. Each student can only be part of at most one pair. What is the maximum number of pairs that can be formed?

i/p:
3-->Test cases
xy
xyxxy
yy

o/p:
1
2
0

"""


for _ in range(int(input())):
    s = input()
    i = 0
    pairs = 0
    while True:
        try:
            if s[i] != s[i+1]:
                pairs += 1
                i += 2
            else:
                i += 1
        except IndexError:
            break
    print(pairs)
