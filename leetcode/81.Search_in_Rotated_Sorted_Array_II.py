#There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Time Complexity: O(n) and Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target in nums:
            return True
        return False
