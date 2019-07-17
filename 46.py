class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        anslist=[]
        start=0
        end=len(nums)-1
        def perm(start,end):
            if start==end:
                anslist.append(nums[:])
            for i in range(start,end+1):
                nums[start],nums[i]=nums[i],nums[start]
                perm(start+1,end)
                nums[start], nums[i] = nums[i], nums[start]
        perm(start,end)
        return anslist

if __name__ == '__main__':
    ans = Solution().permute([1,2,3])
    print ans