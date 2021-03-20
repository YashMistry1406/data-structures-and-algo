def bestsum(targetSum,numbers,memo={}):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum ==0 :
        return []
    if targetSum <0:
        return None

    shortestsum=[]

    for nums in numbers:
        rem=targetSum-nums
        remCombination=bestsum(rem,numbers,memo)
        if remCombination!= None:
            result=remCombination.append(nums)
            if len(shortestsum)==0 or len(result)< len(shortestsum):
                shortestsum=result
    memo[targetSum]=shortestsum
    return shortestsum

n=int(input())
num=list(map(int,input().split()))
print(bestsum(n,num))

