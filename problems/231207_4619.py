from sys import stdin
input = stdin.readline

li = []

while True:
    B,N = map(int, input().split())
    if B == 0 and N == 0:
        break
    A = 0
    while A**N<B:
        A+=1
    
    if A**N-B < B-(A-1)**N:
        result = A
    else:
        result = A-1
        
    li.append(result)

print(*li, sep='\n')