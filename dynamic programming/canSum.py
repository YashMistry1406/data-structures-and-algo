'''
THE COMPLEXITY OF THE BELOW ANSWER


'''
def canSum(targetSum,numbers):
    if targetSum==0: 
        return True
    if targetSum<0:
        return False

    for i in numbers:
        #we subtract the current sum with the targetSum so that 
        #we get a new targetSum and we iterate through it 
        rem=targetSum-i
        if canSum(rem,numbers)==True:
            return True
    return False
n=int(input())
num=list(map(int,input().split()))
print(canSum(n,num))
