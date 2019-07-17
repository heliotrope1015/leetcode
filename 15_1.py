class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        list=[]
        for i in range(0,len(nums)-2):
            if i==0 or(i >0 and nums[i-1]!=nums[i]):
                l=i+1
                r=len(nums)-1
                sums=0-nums[i]
                while l<r:
                    if nums[r]+nums[l]==sums:
                        list.append([nums[i],nums[r],nums[l]])
                        while l<r and nums[l]==nums[l+1]:l+=1
                        while l<r and nums[r]==nums[r-1]:r-=1
                        l+=1
                        r-=1
                    elif  nums[r]+nums[l]>sums:
                        while l<r and nums[r]==nums[r-1]:r-=1
                        r-=1
                    else:
                        while l<r and nums[l]==nums[l+1]:l+=1
                        l+=1
        return list



if __name__ == '__main__':
    ans = Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
    print ans
