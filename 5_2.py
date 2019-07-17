#coding=utf-8
# 动态规划
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = len(s)
        matrix = [[0 for i in range(k)] for i in range(k)]
        logestSubStr = ""
        logestLen = 0
        if k <=1:
            return s

        for j in range(0, k):
            for i in range(0, j + 1):
                if j - i == 0:
                    matrix[i][j] = 1
                    if logestLen < j - i + 1:
                        logestSubStr = s[i:j + 1]
                        logestLen = j - i + 1
                if j - i == 1:
                    if s[i] == s[j]:
                        matrix[i][j] = 2
                        if logestLen < j - i + 1:
                            logestSubStr = s[i:j + 1]
                            logestLen = j - i + 1
                    else:
                        matrix[i][j]=0

                elif j-i>1:
                    if s[i] == s[j] and matrix[i + 1][j - 1]:
                        matrix[i][j] = matrix[i + 1][j - 1]+2
                        if logestLen < j - i + 1:
                            logestSubStr = s[i:j + 1]
                            logestLen = j - i + 1
                    else:
                        matrix[i][j]=0
        return logestSubStr

if __name__ == '__main__':
    strs=Solution().longestPalindrome('cb')
    print strs

# for j in range(0, k):
#     for i in range(0, j + 1):
#         if j - i <= 1:
#             if s[i] == s[j]:
#                 matrix[i][j] = 1
#
#                 if logestLen < j - i + 1:
#                     logestSubStr = s[i:j + 1]
#                     logestLen = j - i + 1
#         else:
#             if s[i] == s[j] and matrix[i + 1][j - 1]:
#                 matrix[i][j] = 1
#                 if logestLen < j - i + 1:
#                     logestSubStr = s[i:j + 1]
#                     logestLen = j - i + 1
# return logestSubStr
