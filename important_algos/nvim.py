stack=list(map(int,input().split()))

n=len(stack)
prefix_sum=[0]*n
prefix_sum[0]=stack[0]
for i in range(1,n):
    prefix_sum[i]=prefix_sum[i-1]+stack[i]
print(prefix_sum)

