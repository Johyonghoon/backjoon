# 1463번 1로 만들기
# https://www.acmicpc.net/problem/1463

n = int(input())
d = [0, 0] + [10**6+1 for _ in range(n-1)]
for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[n])
