class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col=[0 for i in range(n)]
        leftd=[0 for i in range(2*n-1)]
        rightd=[0 for i in range(2*n-1)]
        anslist=[]
        now=[]
        def isvalid(index,i):
            if col[i]==0 and leftd[index - i + n - 1] == 0 and rightd[index + i] == 0:
                return True
            return False
        def placeq(index,i):
            col[i]=1
            leftd[index-i+n-1]=1
            rightd[index+i]=1
        def removeq(index, i):
            col[i] = 0
            leftd[index - i + n - 1] = 0
            rightd[index + i] = 0
        def dfs(index):
            if index==n:
                anslist.append(now[:])
                return
            for i in range(n):
                if isvalid(index,i):
                    placeq(index,i)
                    now.append(i)
                    dfs(index+1)
                    removeq(index,i)
                    now.pop()
        dfs(0)
        lastans = []
        for list in anslist:
            ans = [['.' for i in range(n)] for i in range(n)]
            for i in range(len(list)):
                ans[i][list[i]] = 'Q'
                ans[i]="".join(ans[i])
            lastans.append(ans)
        return lastans
if __name__ == '__main__':
    ans = Solution().solveNQueens(4)
    print ans