def solve(arr):
    return True


stack=list(map(int,input().split()))

if sum(stack)%2 !=0:
    print("False")
else:
    solve(stack)
