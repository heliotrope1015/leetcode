from itertools import product
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []
        numdict={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o,'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        lists=[numdict[digits[i]] for i in range(len(digits))]
        # print lists
        anslist=[]
        for item in product(*lists):
            stritem=''.join(item)
            anslist.append(stritem)
        return anslist
if __name__ == '__main__':
    ans = Solution().letterCombinations("234")
    print ans