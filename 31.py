class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>=nums[i+1]:
                if i==0:
                    nums.reverse()
                else:
                    continue
            else:
                for j in range(i+2,len(nums)+1):
                    if j == len(nums) or nums[i]>=nums[j]:
                        nums[i],nums[j-1]=nums[j-1],nums[i]
                        n=nums[i+1:]
                        n.reverse()
                        nums[i+1:]=n
                        # print nums
                        break
                break
        return nums




if __name__ == '__main__':
    nums=[3,2,1]
    ans=Solution().nextPermutation(nums)
    print nums

