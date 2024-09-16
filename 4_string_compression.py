'''Problem: Given a string s, compress it using the counts of repeated characters. 
For example, "aabcccccaaa" would become "a2b1c5a3". If the compressed string is not shorter
than the original string, return the original string.
'''
class solution:
    def compressed(self,s=str)->str:
        res=""
        a=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                a=a+1
            if s[i]!=s[i+1]:
                res+=s[i]+str(a)
                a=1 
            if i==(len(s)-2):
                res+=s[i+1]+str(a)
            
        return res
    
obj=solution()
print(obj.compressed("aabcccccaaa"))
print(obj.compressed("aaaaaadddddddddbbbbbbbccccchjkta"))


