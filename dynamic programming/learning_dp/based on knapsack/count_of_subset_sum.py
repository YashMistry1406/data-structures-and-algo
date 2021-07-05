#the following code is just the variation in the subset()sum code 
#the only change we have made here is changing the true statements to 1 and False to 0 
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2JEVHVjT1NoWkt2akowQUxfTlV5bm8ycE5fZ3xBQ3Jtc0tsaEk0ZV9DVllyZVo5ZkdILTNhRUwyOHItU1dvZ3VFZlJiS0J5eGZhY1hIcUwzc2F0bERvdXgyWDFrOFJoYUo5S08tQkV3Y1VMTTVwUVhuN2VkWmsxZHJyend4QzF0cUVxSWIycW1jR1l6UkRzSDdkWQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fcount-of-subsets-with-sum-equal-to-x%2F
def subset(stack,n,target):

    memo=[[0 for _ in range(target+1)] for z in range(n+1)]

    for i in range(n+1):
        memo[i][0]=1

    for j in range(1,target+1):
        memo[0][j]=0


    for i in range(1, n + 1):
        for j in range(1, target+ 1):
            if j<stack[i-1]:
                memo[i][j] = memo[i-1][j]
            if j>= stack[i-1]:
                memo[i][j] = (memo[i-1][j] + memo[i - 1][j-stack[i-1]])
               # in the above we have turned the or to + as we have the return type of int as compared to hte boolean in the subetsum code 

    return memo[n][target]

if __name__=='__main__':
    stack=[2,3,5,6,8,10]
    target=10
    n = len(stack)
    print(subset(stack,n,target))
