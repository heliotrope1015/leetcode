class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict={'[':']','{':'}','(':')'}
        stacklist=[]
        if s=='':
            return True
        else:
            for i in range(0,len(s)):
                if stacklist==[]:
                    stacklist.append(s[i])
                    continue
                if stacklist[-1] in dict.keys() and dict[stacklist[-1]]==s[i]:
                    stacklist.pop()
                else:
                    stacklist.append(s[i])
            if stacklist==[]:
                return True
            else:
                return False




if __name__ == '__main__':
    ans = Solution().isValid("([)[]")
    print ans