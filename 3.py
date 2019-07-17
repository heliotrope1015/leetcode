class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        win = []
        ans = 0
        for j in range(len(s)):
            if s[j] in win:
                l = win.index(s[j])
                ans = max(ans, len(win))
                del win[:l + 1]
            win.append(s[j])
            j += 1
        return max(ans, len(win))
