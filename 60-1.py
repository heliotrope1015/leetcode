#coding=utf-8
class Solution:
    def getPermutation(self, n, k):
        if n == 0:
            return []
        nums = [i + 1 for i in range(n)]
        used = [False for _ in range(n)]
        return self.__dfs(nums, used, n, k, 0, [])
    def __factorial(self, n): # 这种编码方式包括了 0 的阶乘是 1 这种情况
        res = 1
        while n:
            res *= n
            n -= 1
        return res
    def __dfs(self, nums, used, n, k, depth, pre):
        if depth == n: # 在叶子结点处结算
            return ''.join(pre) # 后面的数的全排列的个数
        ps = self.__factorial(n - 1 - depth)
        print(ps)
        for i in range(n): # 如果这个数用过，就不再考虑
            if used[i]:
                continue # 后面的数的全排列的个数小于 k 的时候，执行剪枝操作
            if ps < k:
                k -= ps
                continue
            pre.append(str(nums[i])) # 因为直接走到叶子结点，因此状态不用恢复
            used[i] = True
            return self.__dfs(nums, used, n, k, depth + 1, pre)


if __name__ == '__main__':
    ans=Solution().getPermutation(3,4)
    print ans