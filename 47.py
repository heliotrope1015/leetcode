class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        anslist=[]
        start=0
        end=len(nums)-1
        def isswap(start,i):
            for j in range(start,i):
                if nums[i]==nums[j]:
                    return False
            return True


        def perm(start,end):
            if start==end:
                anslist.append(nums[:])
            for i in range(start,end+1):
                if isswap(start,i):
                    nums[start],nums[i]=nums[i],nums[start]
                    perm(start+1,end)
                    nums[start], nums[i] = nums[i], nums[start]
        perm(start,end)
        return anslist

if __name__ == '__main__':
    ans = Solution().permuteUnique([1,1,2,2])
    print ans