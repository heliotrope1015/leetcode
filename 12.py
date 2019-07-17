class Solution(object):
    def intToRoman(self, num):
        intlist=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romlist=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        ans=''
        i=0
        while i < len(intlist):
            if num>=intlist[i]:
                ans=ans+romlist[i]
                num=num-intlist[i]
            else:
                i=i+1
        return ans


if __name__ == '__main__':
    ans=Solution().intToRoman(333)
    print ans