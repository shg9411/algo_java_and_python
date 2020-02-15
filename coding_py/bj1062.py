from itertools import combinations
import sys
n, k = map(int, sys.stdin.readline().split())

if k < 5:
    print(0)
    sys.exit()
if k == 26:
    print(n)
    sys.exit()
text = []
alpha = set('acint')
check = set()

for _ in range(n):
    word = set(sys.stdin.readline().strip())
    text.append(word)
    check = check.union(word)
check = check-alpha
tmp = 0

for c in combinations(check, min(k-5, len(check))):
    count = 0
    subset = set(c).union(alpha)
    for word in text:
        if word.issubset(subset):
            count += 1
    if tmp < count:
        tmp = count
print(tmp)