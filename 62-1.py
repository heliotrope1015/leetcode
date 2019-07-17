class Solution:
    def uniquePaths(self, m, n):
        cur = [1] * n
        for i in range(1,m):
            for j in range(1, n):
                cur[j]+=cur[j-1]
        return cur[-1]
if __name__ == '__main__':
    ans = Solution().uniquePaths(7,3)
    print ans
