from sys import stdin
input = stdin.readline

k = int(input())
d1,d2 = map(int,input().split())

if d1 == d2:
    print(k*k)
else:
    tmp = (d1-d2)/2
    print(k*k  - tmp * tmp)