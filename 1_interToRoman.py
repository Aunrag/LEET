class solution:
    def convert(self,n:int)->str:
        if n not in range(1,4000):
            o="number out range"
            return o
        r=""
        p=str(n)
        s=(p[::-1])
        
        for i in range(len(s)):
            if i==0:
                r1=""
                if int(s[i])<4:
                    r1+=int(s[i])*"I"
                if int(s[i])==4:
                    r1+="IV" 
                if int(s[i])>=5 and int(s[i])<9:
                    k=int(s[i])-5
                    r1+="V"+(k*"I")
                if int(s[i])==9:
                    r1+="IX"
                r+=r1[::-1]
            if i==1:
                r2=""
                if int(s[i])<4:
                    r2+=int(s[i])*"X"
                if int(s[i])==4:
                    r2+="XL"
                if int(s[i])>=5 and int(s[i])<9:
                    k=(int(s[i])-5)
                    r2+="L"+(k*"X")
                if int(s[i])==9:
                    r2+="XC"
                r+=r2[::-1]
            
            if i==2:
                r3=""
                if int(s[i])<4:
                    r3+=int(s[i])*"C"
                if int(s[i])==4:
                      r3+="CD"
                if int(s[i])>=5 and int(s[i])<9:
                    k=(int(s[i])-5)
                    r3+="D"+(k*"C")
                if int(s[i])==9:
                      r3+="CM"
                r+=r3[::-1]
                    
            if i==3:
                r4=""
                if int(s[i])<5:
                    r4+=int(s[i])*"M"
                r+=r4[::-1]
                    
        return r[::-1]
    
obj=solution()
print(obj.convert(3749))
print(obj.convert(58))
print(obj.convert(1994))
print(obj.convert(-1994))
print(obj.convert(3999))
print(obj.convert(4999))
print(obj.convert(1234))
