class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        anslist=[]
        now=[]
        res=target
        def dfs(res,min):
            if res==0:
                anslist.append(now[:])
                return
            for i in range(min,len(candidates)):
                if res-candidates[i]<0:
                    break
                else:
                    res=res-candidates[i]
                    now.append(candidates[i])
                    dfs(res,i)
                    res=res+candidates[i]
                    now.pop()
        dfs(res,0)
        return anslist


if __name__ == '__main__':
    ans = Solution().combinationSum([2,3,6,7],7)
    print ans