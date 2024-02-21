# leetcode Question Two Sumclass Solution:
# approch : hashing 
# time complexity:O(n) space complexity:O(n) where n is the length of the nums

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return [hash_map[nums[i]],i]
            hash_map[target-nums[i]]=i

# Driver Code
# i changed something
