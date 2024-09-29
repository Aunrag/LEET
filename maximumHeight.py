'''Q. Maximize the Total Height of Unique Towers
You are given an array maximumHeight, where maximumHeight[i] denotes the maximum height the ith tower can be assigned.

Your task is to assign a height to each tower so that:

The height of the ith tower is a positive integer and does not exceed maximumHeight[i].
No two towers have the same height.
Return the maximum possible total sum of the tower heights. If it's not possible to assign heights, return -1.

Example 1:

Input: maximumHeight = [2,3,4,3]

Output: 10

Explanation:

We can assign heights in the following way: [1, 2, 4, 3]. 
'''
from typing import List

class Solution:
    def maxHeight(self, a: List[int]) -> int:
        for k in range(len(a)):
            for i in range(len(a)):
                if a[i]<=0:
                    return -1
                for j in range(len(a)):
                    if i!=j and a[i]==a[j]:
                        a[i]=a[i]-1
        sum=0              
        for m in range(len(a)):
            sum=sum+a[m]
        return sum
                        
obj=Solution()
print(obj.maxHeight([2,3,3,4]))
print(obj.maxHeight([15,10]))
print(obj.maxHeight([2,2,1]))