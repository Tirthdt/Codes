"""
Chef has an integer N and he wants to generate a matrix M with N rows (numbered 1 through N) and N columns (numbered 1 through N). He thinks that M would be delicious if:

Each element of this matrix is an integer between 1 and N2 inclusive.
All the elements of the matrix are pairwise distinct.
For each square submatrix containing cells in rows r through r+a and in columns c through c+a (inclusive) for some valid integers r, c and a≥0:
Mr,c+Mr+a,c+a is even
Mr,c+a+Mr+a,c is even
Can you help Chef generate a delicious matrix? It can be proved that a solution always exists. If there are multiple solutions, you may find any one.
"""

for _ in range(int(input())):
    n = int(input())
    mat = []
    i = 1
    while i <= n**2:
        t = []
        for j in range(n):
            t.append(i)
            i += 1
        mat.append(t)
    if n % 2 == 0:
        for i in range(1, n, 2):
            for j in range(0, n, 2):
                mat[i][j], mat[i][j+1] = mat[i][j+1], mat[i][j]
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()
