class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col=set()
        leftd=set()
        rightd=set()
        global nums
        nums=0
        now=[]
        def isvalid(index,i):
            if i not in col and index + i not in leftd and index - i not in rightd:
                return True
            return False
        def placeq(index,i):
            col.add(i)
            leftd.add(index+i)
            rightd.add(index-i)
        def removeq(index, i):
            col.remove(i)
            leftd.remove(index + i)
            rightd.remove(index - i)
        def dfs(index):
            global nums
            if index==n:
                nums+=1
                return
            for i in range(n):
                if isvalid(index,i):
                    placeq(index,i)
                    # now.append(i)
                    dfs(index+1)
                    removeq(index,i)
                    # now.pop()
        dfs(0)
        return nums
if __name__ == '__main__':
    ans = Solution().totalNQueens(4)
    print ans