class Solution(object):
    def nthUglyNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # ugltset=set(1,2,3,5)
        clist=[1]
        i=0
        i1,i2,i3=0,0,0
        while i<num-1:
            miner=min(clist[i1]*2,clist[i2]*3,clist[i3]*5)
            clist.append(miner)
            if miner==clist[i1]*2:
                i1+=1
            if miner==clist[i2]*3:
                i2+=1
            if miner==clist[i3]*5:
                i3+=1
            i+=1
        return clist[-1]


if __name__ == '__main__':
    ans = Solution().nthUglyNumber(10)
    print ans
