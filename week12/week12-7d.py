a=list(map(int,input().split()))
ans=0
N=len(a)
for i in range(N):
	if a[i]>0:	
		ans+=a[i]
print(ans,end='')