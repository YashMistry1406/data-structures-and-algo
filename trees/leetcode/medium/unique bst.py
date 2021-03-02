class Solution:
    def numTrees(self, n: int) -> int:
        def factorial(n):  
            if (n==1 or n==0): 
                return 1
            else: 
                return (n * factorial(n - 1)) 
        return int(factorial(2*n)/(factorial(n)*factorial(n+1)))
        
            
            
        
