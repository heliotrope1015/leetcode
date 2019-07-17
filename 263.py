class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # ugltset=set(1,2,3,5)
        if num <= 0:
            return False
        while num%2==0:
            num/=2
        while num%3==0:
            num/=3
        while num%5==0:
            num/=5
        if num==1:
            return True
        else:
            return False

if __name__ == '__main__':
    ans = Solution().isUgly(14)
    print ans