class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = []
        a,b = 0,0
        while b != n:
            while a != m:
                if nums1[a] <= nums2[b]:
                    nums.append(nums1[a])
                    a += 1
                else: # nums1[a] > nums2[b]
                    nums.append(nums2[b])
                    b += 1
        nums1 = nums
        
