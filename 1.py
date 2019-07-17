class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            b = target - nums[i]
            if b in nums:
                c = nums.index(b)
                if i != c:
                    return [i, c]
