def palindrome(s):
    return s[::-1]==s
def solve(s,i,j):
    if i>=j:
        return 0
    if palindrome(s[i:j + 1]) ==True:
        return 0
    # k=i
    mn=float('inf')
    temp=0
    for k in range(i,j):
        temp=(1+ solve(s,i,k)+solve(s,k+1,j))
        if temp<mn:
            mn=temp
        k+=1
    return mn
