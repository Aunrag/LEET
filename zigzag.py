class solution:
    def conevert(self,s: str,numrow:int)-> str:
        if numrow==1 :
            return s
        res=""
        for r in range(numrow):
            increment=2*(numrow-1)
            for i in range(r,len(s),increment):
                res+=s[i]
                if (r>0 and r< numrow-1 and( i + increment -2*r) < len(s)):
                    res+= s[i+ increment-2*r]
        return res
    
obj=solution()
a="paypalishiring"
print(obj.conevert(a,3))

