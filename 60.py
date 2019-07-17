class Solution(object):
    count=0
    visit=[]
    numlist=[]
    k=0
    flag=0
    ans=[]
    def dfs(self,index):
        if index==len(self.nums):
            # print self.numlist
            self.count+=1
            if self.count>=self.k:
                return self.numlist
        else:
            for i in range(len(self.nums)):
                if self.visit[i]==0:
                    self.numlist[index]=self.nums[i]
                    self.visit[i]=1
                    if self.dfs(index+1)==self.numlist:
                        return self.numlist
                    self.visit[i] = 0
    def getPermutation(self, n, k):
        self.nums=[i for i in range(1,n+1)]
        self.visit=[0 for i in range(0,n)]
        self.numlist=[0 for i in range(0,n)]
        self.k=k

        anslist= self.dfs(0)
        ans=''.join(map(str,anslist))
        return ans
        # print self.ans
if __name__ == '__main__':
    ans=Solution().getPermutation(3,4)
    print ans

