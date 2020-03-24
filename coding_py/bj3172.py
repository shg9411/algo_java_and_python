import sys
input = sys.stdin.readline

a = [0 for _ in range(100001)]


def get(x):
    t = 0
    while x > 0:
        t += a[x]
        x -= (x & -x)
    return t


def update(x):
    while x <= 100000:
        a[x] += 1
        x += (x & -x)


n = int(input())
tmp = []
for _ in range(n):
    word = input().rstrip()
    tmp.append([word, word[::-1], 0, 0])

tmp.sort(key=lambda x: x[0])
for i in range(n):
    tmp[i][2] = n-i
tmp.sort(key=lambda x: x[1])
for i in range(n):
    tmp[i][3] = n-i
#print(tmp)
res = 0
for i in range(n):
    res += get(tmp[i][2])
    update(tmp[i][2])

print(res)
