import sys
input = sys.stdin.readline

before = input().rstrip()
after = input().rstrip()
bl = len(before)
al = len(after)
length = min(al, bl)
idx = -1
for i in range(length):
    idx = i
    if after[i] != before[i]:
        break

length -= idx
diff = length
for i in range(length):
    if after[al-i-1] != before[bl-i-1]:
        diff = i
        break

print(al - diff - idx)
