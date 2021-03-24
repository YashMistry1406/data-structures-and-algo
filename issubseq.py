def isSubsequence(s,t):
    memo={}
    string=""
    for j in s:
        if j not in memo:
            memo[j]=0
        if j in memo:
            memo[j]+=1
    print(memo)
    for i in t:
        if i in s:
            if memo[i] !=0:
                memo[i]-=1
                string+=i
        else:
            continue
    print(string)
    if string==s:
        return True 
    else:
        return False

s=input()
t=input()
print(isSubsequence(s,t))
