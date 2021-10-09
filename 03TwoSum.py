class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            val = target-nums[i]
            if val in nums:
                poss = nums.index(val)
                if i != poss:
                    return (i,poss)

# EOF #
