class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numdict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        i=0
        ans=0
        while i<len(s):
            if i< len(s)-1 and numdict[s[i]]<numdict[s[i+1]]:
                ans=ans+(numdict[s[i+1]]-numdict[s[i]])
                i+=2
            else:
                ans=ans+numdict[s[i]]
                i+=1
        return ans

if __name__ == '__main__':
    ans=Solution().romanToInt('MCMXCIV')
    print ans