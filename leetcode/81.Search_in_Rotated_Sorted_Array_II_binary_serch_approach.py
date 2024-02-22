# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Time Complexity:O(log n) and Space Complexity: O(1) 
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return True
            if nums[left]==nums[mid]==nums[right]:
                left+=1
                right-=1
            elif nums[mid]>=nums[left]:
                if target<nums[left] or target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if target<nums[mid] or nums[right]<target:
                    right=mid-1
                else:
                    left=mid+1
        return False
