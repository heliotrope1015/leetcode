class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        anslist=[]
        now=[]
        res=target
        def dfs(res,min):
            if res==0:
                anslist.append(now[:])
                return
            for i in range(min,len(candidates)):
                if i>0 and candidates[i]==candidates[i-1] and i-1>=min:
                    continue
                if res-candidates[i]<0:
                    break
                else:
                    res=res-candidates[i]
                    now.append(candidates[i])
                    dfs(res,i+1)
                    res=res+candidates[i]
                    now.pop()
        dfs(res,0)
        return anslist


if __name__ == '__main__':
    ans = Solution().combinationSum2([10,1,2,7,6,1,5],8)
    print ans