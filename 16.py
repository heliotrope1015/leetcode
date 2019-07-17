class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        list=[]
        ansdict={}
        for i in range(0,len(nums)-2):
            l=i+1
            r=len(nums)-1
            sum=target-nums[i]
            while l<r:
                sums = nums[i] + nums[l] + nums[r]
                dis = abs(sums - target)
                ansdict[dis] = sums
                if nums[r]+nums[l]==sum:
                    return sum
                elif  nums[r]+nums[l]>sum:
                    r-=1
                else:
                    l+=1
        key_min = min(ansdict.keys())
        return ansdict[key_min]
if __name__ == '__main__':
    ans = Solution().threeSumClosest([0,0,0],1)
    print ans