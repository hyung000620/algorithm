from sys import stdin
input = stdin.readline

x1,y1,r1 = map(int,input().split())
x2,y2,r2 = map(int,input().split())

x = (x2-x1)**2
y = (y2-y1)**2
r = (r2+r1)**2

print("YES" if r > x+y else "NO")