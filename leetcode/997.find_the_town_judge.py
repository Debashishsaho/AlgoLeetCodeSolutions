# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge. If the town judge exists, then:
# 1) The town judge trusts nobody.
# 2) Everybody (except for the town judge) trusts the town judge.
# 3) There is exactly one person that satisfies properties 1 and 2.

# Time Complexity: O(n+t) Space Complexity : O(n)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        person=[0]*(n+1)
        for a,b in trust:
            person[b] +=1
            person[a] -=1
        for i in range(1,n+1):
            if person[i]==n-1:
                return i 
        return -1

# Driver Code
