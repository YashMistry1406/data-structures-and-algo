'''
THE COMPLEXITY OF THE BELOW ANSWER



'''
def canSum(targetSum,numbers,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum==0:
        return True
    if targetSum<0:
        return False

    for i in numbers:
        #we subtract the current sum with the targetSum so that 
        #we get a new targetSum and we iterate through it 
        rem=targetSum-i
        if canSum(rem,numbers,memo)==True:
            memo[targetSum]=True
            return True
    memo[targetSum]=False
    return False
n=int(input())
num=list(map(int,input().split()))
print(canSum(n,num))
