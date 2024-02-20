## buteforce approach Time Complexity : O(n) and Space Complexity : O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums2)
        n=len(nums1)
        res=[0]*(m+n)
        i=0
        j=0
        k=0
        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                res[k]=nums1[i]
                i+=1
                k+=1
            else:
                res[k]=nums2[j]
                j+=1
                k+=1
        while i<n:
            res[k]=nums1[i]
            i+=1
            k+=1
        while j<m:
            res[k]=nums2[j]
            j+=1
            k+=1
        if (m+n)%2==0:
            return (res[(m+n-1)//2]+res[((m+n-1)//2)+1])/2
        else:
            return res[(m+n-1)//2]
## Driver Code
