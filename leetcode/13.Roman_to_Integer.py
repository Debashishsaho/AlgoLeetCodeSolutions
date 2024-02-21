# Roman to Integer 
# Time Complexity : O(n) where n is length of the string , Space Complexity : O(1) it takes constant space 

class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        digit=hash_map[s[0]]
        for i in range(1,len(s)):
            if s[i] in hash_map:
                digit+=hash_map[s[i]]

            if hash_map[s[i-1]]<hash_map[s[i]]:
                digit-=2*hash_map[s[i-1]]
            else:
                continue
        return digit

# Driver Code
