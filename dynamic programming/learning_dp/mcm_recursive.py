def solve(arr, i , j):

    if i>=j:
        return 0
    mn=float('inf')
    k=i
    for k in range(i,j):
        temp=solve(arr,i,k)+solve(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]

        if temp<mn:
            mn=temp
    return mn
arr=[1,2,3,4,3]
n=len(arr)
print(solve(arr,1,n-1))

