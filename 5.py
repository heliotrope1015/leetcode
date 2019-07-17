
#coding=utf-8
# 完全暴力法
class Solution(object):
    def check(self, first, last, s):
        i = first
        j = last
        while j - i >= 0:
            if s[i] != s[j]:
                return '0'
            else:
                i += 1
                j -= 1
        return s[first:last+1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        ans = 0
        if len(s)<=1:
            return s
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                strs = self.check(i, j, s)
                if len(strs)>ans:
                    maxstr=strs
                    ans=len(strs)
        return maxstr


if __name__ == '__main__':
    strs=Solution().longestPalindrome('aaaaaaaaaaaaa')
    print strs
