#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTBWZlFGQ3A3NnNJdjVRZzc0SHVuem9wQmhvd3xBQ3Jtc0tuRWpFVmk4SURPbERVMW1JbjRPSzF3V3kwR18wbGVvUzZNaXJtaFlEMG5LN0FneG9KbFZQcHdnWldFWlpzOC03a05pU0x6VjB0TlkwVWdqQVZLbExFUEl4dFlycXZTWXJsS2xaQ0RpZjRHSUNlUnpaSQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fsubset-sum-problem-dp-25%2F
from typing import Sized


def subset(stack,n,target):

    memo=[[False for _ in range(target+1)] for z in range(n+1)]

    for i in range(n+1):
        memo[i][0]=True

    for j in range(1,target+1):
        memo[0][j]=False
        
    for i in range(1, n + 1):
        for j in range(1, target+ 1):

            print(j)
            if j<stack[i-1]:
                memo[i][j] = memo[i-1][j]
            if j>= stack[i-1]:
                memo[i][j] = (memo[i-1][j] or memo[i - 1][j-stack[i-1]])

    return memo[n][target]
if __name__=='__main__':
    stack= [3, 34, 4, 12, 5, 2]
    target=9
    n = len(stack)
    print(subset(stack,n,target))
'''
 sum        0    1    2    3    4    5    6
array elements
0           T    F    F    F    F    F    F

3           T    F    F    T    F    F    F

4           T    F    F    T    T    F    F   
              
5           T    F    F    T    T    T    F

2           T    F    T    T    T    T    T

'''
