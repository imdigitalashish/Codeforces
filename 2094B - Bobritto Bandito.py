t =int(input())
print("\n\n")
for _ in range(t):
    n,m,l,r = map(int,input().split())
    print(max(-m,l),max(-m,l)+m)
