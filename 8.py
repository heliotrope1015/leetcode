class Solution(object):

    def myAtoi(self, str):
        table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-','+']
        table1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if str=='':
            return 0
        for i in str:
            if i==' ':
                str=str[1:]
            else:break
        # print str
        if str=='':
            return 0
        if str[0] not in table:
            return 0
        else:
            ans=str[0]
            for i in range(1,len(str)):
                if str[i] not in table1:
                    if ans == '' or ans == '-' or ans == '+':
                        return 0
                    else:
                        if int(ans) < -2147483648:
                            ans = -2147483648
                        if int(ans) > 2147483647:
                            ans = 2147483647
                        return int(ans)
                else:
                    ans=ans+str[i]
        if ans == '' or ans == '-' or ans == '+':
            return 0
        if int(ans) <-2147483648:
            ans=-2147483648
        if int(ans)>2147483647:
            ans=2147483647
        return int(ans)

if __name__ == '__main__':
    ans=Solution().myAtoi('   -9456846124846484642ee')
    print ans
