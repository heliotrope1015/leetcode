class Solution(object):
    def reverse(self, x):
        str1=str(x)
        if str1[0]=='-':
            str2=str1[len(str1):0:-1]
            # print str2
            ans=-1*int(str2)
        else:
            str2=str1[::-1]
            ans=int(str2)
        if ans<-2147483648 or ans>2147483647:
            ans=0
        return ans

if __name__ == '__main__':
    strs=Solution().reverse(23334456567878989)
    print strs