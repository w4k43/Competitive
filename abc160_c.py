k,n = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(1, n):
    b.append(a[i]-a[i-1])
b.append(a[0]+k-a[-1])
print(k-max(b))