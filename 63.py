class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid[0])
        n=len(obstacleGrid)
        # print m ,n
        dp=[[0 for i in range(m)]for j in range(n)]
        for i in range(m):
            if obstacleGrid[0][i]!=1:
                dp[0][i]=1
            else:
                dp[0][i] = 0
                break
        for j in range(n):
            if obstacleGrid[j][0]!=1:
                dp[j][0]=1
            else:
                dp[j][0] = 0
                break
        # print dp
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[j][i] != 1:
                    dp[j][i]=dp[j][i-1]+dp[j-1][i]
                else:
                    dp[j][i]=0
        return dp[n-1][m-1]
if __name__ == '__main__':
    grid=[
  [1,0]
]
    ans = Solution().uniquePathsWithObstacles(grid)
    print ans