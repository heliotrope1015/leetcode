import itertools
class Solution(object):
    def permute(self, nums):
        return list(itertools.permutations(nums))
if __name__ == '__main__':
    ans = Solution().permute([1,2,3])
    print (ans)