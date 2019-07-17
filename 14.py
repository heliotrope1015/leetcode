class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ""
        minlen =min([len(st) for st in strs])
        lens=len(strs)
        ans=''
        if minlen==0:
            return ""
        temp=strs[0]

        for j in range(minlen):
            for i in range(lens):
                if strs[i][j]!=temp[j]:
                    return ans
            ans=ans+strs[i][j]
        return  ans


if __name__ == '__main__':
    ans=Solution().longestCommonPrefix([])
    print ans