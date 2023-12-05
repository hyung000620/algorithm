n = int(input())

res = []
res.append("@"*(n+2))

for i in range(n):
    res.append("@"+" "*n+"@")

res.append("@"*(n+2))

print(*res,sep='\n')