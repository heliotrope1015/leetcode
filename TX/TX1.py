#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip().split(' ')
    m=int(line[0])
    n=int(line[1])
    # ans = 0
    # m=20
    # n=4
    # typelist=[1,2,5,10]
    typelist=[]
    for i in range(n):
        # 读取每一行
        type = sys.stdin.readline().strip()
        typelist.append(int(type))
    lists=[[] for i in range(m+1)]
    print lists
    typelist.sort()
    dp=[0 for i in range(m+1)]
    for i in range(1,m+1):
        if i in typelist:
            dp[i]=1
            lists[i].append(i)
        else:
            for j in range(n):
                if i>=typelist[j]:
                    dp[i]=dp[i-typelist[j]]+1

    print dp








    #
    #
    # for i in range(n):
    #     dicts[i] = 0
    # if typelist[0]!=1:
    #     print -1
    # else:
    #     s=m
    #     while s>0:
    #         if sums>=s:
    #             print dicts
    #             s-=1
    #             sums=0
    #             for i in range(n):
    #                 dicts[i] = 0
    #
    #         else:
    #             num=n-1
    #             while num>=0:
    #                 if typelist[num]<=s-sums:
    #                     sums+=typelist[num]
    #                     dicts[num]=dicts[num]+1
    #                 else:
    #                     num-=1
    #
    #
    #
