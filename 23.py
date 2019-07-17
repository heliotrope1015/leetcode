# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def mergeKLists(self, lists):
        index = []
        ll=ListNode(0)
        ans=ll
        if lists==[]:
            return None

        for i in range(len(lists)):
            l=ListNode(0)
            l.next=lists[i]
            l=l.next
            index.append(l)
        def themin(index):
            tmin = index[0]
            for i in range(1,len(index)):
                if index[i].val<=tmin.val:
                    tmin=index[i]
            return tmin
        while index!=[]:
            for i in range(len(index)):
                tmin = themin(index)
                if index[i]==tmin:
                    ll.next=ListNode(index[i].val)
                    ll=ll.next
                    if index[i].next!=None:
                        index[i] = index[i].next
                    else:
                        index.pop(i)
                        break
        return ans.next
if __name__ == '__main__':
    inlist=[[1,4,5],[1,3,4],[2,6]]
    # inlist=[[]]
    # outlist=[[]]*3
    outlist=[]
    for i in  range(len(inlist)):
        l=ListNode(inlist[i][0])
        # outlist[i]=l                        ans.append(ListNode(index[i].val))
        outlist.append(l)
        for j in inlist[i][1:]:
            l.next=ListNode(j)
            l=l.next

    ans = Solution().mergeKLists(outlist)
    print ans