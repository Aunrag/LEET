class solution:
    def reverse(self,x:int)->int:
        if x< 0 :
            k=str(x*(-1))
            n=k[::-1]
            s=(int(n)*-1)
        else:
            m=str(x)
            n=(m[::-1])
            s=int(n)
        if s in range((-2**31),((2**31)-1)):
            return s
        else:
            return 0
    
obj=solution()
'''a=int(input("enter the number: "))'''
print(obj.reverse(112233))
print(obj.reverse(123654789))
print(obj.reverse(456586))
