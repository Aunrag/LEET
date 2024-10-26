'''Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.

 Example 1:

Input: k = 5

Output: "b"

Explanation:

Initially, word = "a". We need to do the operation three times:

Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd". 
'''
class Solution:
    def kthCharacter(self, k: int) -> str:
        a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        b=["a"]
        for j in range(k):
            for i in range(len(b)):
                c=(a.index(b[i]))
                if(c==(len(a)-1)):
                    b.append(a[0])
                else:
                    b.append(a[c+1])     
        return(b[k-1])
            

obj=Solution()
print(obj.kthCharacter(5))
print(obj.kthCharacter(10))
#print(obj.kthCharacter(25))
#print(obj.kthCharacter(26))


        
