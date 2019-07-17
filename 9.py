class Solution(object):

    def isPalindrome(self, x):
        strs=str(x)
        for i in range(len(strs)):
            j= len(strs)-1-i
            if j<=i:
                return True
            if strs[i]!=strs[j]:
                return False



if __name__ == '__main__':
    ans=Solution().isPalindrome('-121')
    print ans
