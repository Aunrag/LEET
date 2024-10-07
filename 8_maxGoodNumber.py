from typing import List
from itertools import permutations
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        a=self.rearrange(nums)
        f=[]
        for i in range(len(a)):
            b=self.DecimalToBinary(a[i])
            c=""
            for j in range(3):
                c=c+b[j]
            d=self.BinaryToDecimal(c)
            f.append(d)
        return(max(f))
                
    def DecimalToBinary(self,c:List[int]):
         g=[]
         for i in range(min(3, len(c))):
            a=c[i]
            m=""
            x=1
            while(x!=0):
                x=a//2
                y=a/2
                m=m+str(int((y-x)*2))
                a=x
            n=m[::-1]
            g.append(n)
         return(g)
    def rearrange(self,a:List[int])->List[int]:
         perm = list(set(permutations(a)))
         return(perm)

            
        
    def BinaryToDecimal(self,a: str)->int:
           b=a[::-1]
           y=0
           for i in range(len(b)):
               x=(int(b[i]))*(2**i)
               y=y+x
           
           return(y)
            
        
        
            
            
            
      
    
obj=Solution()
print(obj.maxGoodNumber([1,2,3]))
print(obj.maxGoodNumber([2,8,16]))
print(obj.maxGoodNumber([1,38,1]))
print(obj.maxGoodNumber([1,2,1]))
    


