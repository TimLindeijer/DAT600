import numpy as np
# Matrices

#  A1  |   A2  |   A3   |   A4  |  A5
# 5x10 | 10x15 | 15x30  | 30x5  | 5x20

# Means p values:
# p1=5, p2=10, p3=15, p4=30, p5=5, and p6=20

p = [5, 10, 15, 30, 5, 20]

n = len(p)-1

m = np.zeros((5, 5))
s = np.zeros((5, 5))


for l in range(2, n+1):
    for i in range(0, n-l+1):
        j = i + l - 1
        m[i, j] = 999999
        print(f"\n---m[{i+1}][{j+1}]---")
        for k in range(i, j):
            q = m[i, k] + m[k + 1, j] + p[i] * p[k+1] * p[j+1]
            print(f"\tm[{i+1}][{k+1}] + m[{k+2}][{j+1}] + p{i+1}*p{k+2}*p{j+2} = {int(m[i, k])} + {int(m[k + 1, j])} + {p[i]} * {p[k+1]} * {p[j+1]} = {int(q)}")
            if q < m[i, j]:
                m[i, j] = q
                s[i, j] = k

print(m)
print(s)

