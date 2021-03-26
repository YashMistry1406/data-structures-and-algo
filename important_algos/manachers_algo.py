'''
https://www.youtube.com/watch?v=nbTSfrEfo6M
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        c=0
        r=0
        t= '#'.join('^{}$'.format(s))
        n=len(t)
        p=[0]*n
        for i in range(n-1):
            mirr=2*c-i
            if i<r:
                p[i]=min(r-i,p[mirr])
            while t[i+(1+p[i])]==t[i-(1+p[i])]:
                p[i]+=1
                if i+p[i]>r:
                    c=i
                    r=i+p[i]
        maxLen, centerIndex = max((n, i) for i, n in enumerate(p))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
