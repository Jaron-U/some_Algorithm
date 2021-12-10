def LCS_length(x, y):
    m = len(x)
    n = len(y)
    c = [[None]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j==0:
                c[i][j] = 0
            elif x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]

x = ['k','l','m','l','j','k','l']
y = ['l','j','m','k','l','k']
print(LCS_length(x,y))


