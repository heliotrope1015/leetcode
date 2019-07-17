#coding=utf-8
# 改进暴力法
class Solution(object):
    def check(self, first, last, s):
        i = first
        j = last
        while j - i >= 1:
            if s[i] != s[j]:
                return 0
            else:
                i += 1
                j -= 1
        lenth = last - first + 1
        return lenth

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        for l in range(len(s),0,-1):
            for i in range(0,len(s)-l+1):
                if self.check(i,i+l-1,s)!=0:
                    return s[i:i+l]

if __name__ == '__main__':
    strs=Solution().longestPalindrome('aaaaaa')
    print strs
