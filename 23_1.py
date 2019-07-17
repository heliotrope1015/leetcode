# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll1 = ListNode(0)
        ll2 = ListNode(0)
        newl = ListNode(0)
        ans = newl
        ll1.next = l1
        ll2.next = l2
        while ll1.next != None and ll2.next != None:
            if ll1.next.val <= ll2.next.val:
                newl.next = ListNode(ll1.next.val)
                newl = newl.next
                ll1 = ll1.next
            else:
                newl.next = ListNode(ll2.next.val)
                newl = newl.next
                ll2 = ll2.next
        if ll1.next != None:
            newl.next = ll1.next

        if ll2.next != None:
            newl.next = ll2.next
        return ans.next

    def mergeKLists(self, lists):
        l0=lists[0]
        for i in range(1,len(lists)):
            l0=self.mergeTwoLists(l0,lists[i])
        return l0

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