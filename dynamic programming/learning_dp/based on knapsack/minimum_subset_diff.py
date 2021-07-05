#
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2FxeEpra0RQTHhuVERaT0hWZG11aDM4SE42UXxBQ3Jtc0ttVktJYXVFcDFyR0tjeGE4dmw5TDBnRlZPT1F4bVRFaU5ySXFQZTFkR2Y2UzB6enJhbzJtemVRYUUxRzU0azEtQlQ4blM2TVZJcDByQ3pMVzFsVnJ5cnEzVVcwWFhNMWFZRWlrbUtaeGpvMzhDbTZ0SQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fpartition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum%2F
def minisum_subet_diff(arr):
    su=sum(arr)
    n=len(arr)
    memo=[[0 for _ in range(su+1)] for j in range(n+1)]
    j=0
    for l in range(n+1):
        memo[l][0]=True
    for k in range(1,su+1):
        memo[0][k]=False
    for i in range(1,n+1):
        for j in range(1,su+1):

            if j<stack[i-1]:
                memo[i][j] = memo[i-1][j]
            if j>=arr [i-1]:
                memo[i][j] = (memo[i-1][j] or memo[i - 1][j-arr[i-1]])
    diff=float('inf ')
    for s in range(su//2,-1,-1):
        if memo[n][s]==True:
            diff=su-(2*s)
            break
    return diff







stack=list(map(int,input().split()))
print(minisum_subet_diff(stack))
