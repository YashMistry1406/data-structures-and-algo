def howsum(targetsum,numbers,memo={}):
    #the following are the bse cases in which we are checking the final condition of the tree(refer the png image for tree representation)
    #since the sum will  never be less than 0 that is -ve
    #if we reach 0 that means the path used to reach is valid and we can form the targetsum using the following path 

    if targetsum in memo:
        return memo[targetsum]
    if targetsum ==0:
        return []
    if targetsum<0:
        return None

    #in the following  
    for num in numbers:
        rem=targetsum-num
        result=howsum(rem,numbers,memo)
        if result!=None:
            memo[targetsum]=result.append(num)
            return memo[targetsum]
    memo[targetsum]=None
    return memo[targetsum]

n=int(input())
num=list(map(int,input().split()))
print(howsum(n,num))
