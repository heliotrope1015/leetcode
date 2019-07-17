class Solution(object):
    def convert(self, s, numRows):
        down=False
        strs=''
        numRows=min(numRows,len(s))
        row=[[] for i in range(numRows)]
        r=0
        if numRows==1:
            return s
        for i in range(0,len(s)):
            row[r].append(s[i])
            if r==0 or r==numRows-1:
                down=not down
            if down:
                r+=1
            else:
                r-=1
        for i in range(numRows):
            strs=strs+''.join(row[i])
        return strs
if __name__ == '__main__':
    strs=Solution().convert('niuuhdshiufs',1)
    print strs