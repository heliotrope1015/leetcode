# coding=utf-8
# class Solution(object):
#     def backtrack(self,S, left, right,ans,N):
#         if len(S) == 2 * N:
#             ans.append(S)
#             return
#         if left < N:
#             Solution().backtrack(S + '(', left + 1, right,ans,N)
#         if right < left:
#             Solution().backtrack(S + ')', left, right + 1,ans,N)
#     def generateParenthesis(self, N):
#         ans = []
#         Solution().backtrack('',0,0,ans,N)
#         return ans

#函数嵌套
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans


if __name__ == '__main__':
    ans = Solution().generateParenthesis(3)
    print ans
