# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        llen=0
        nllen=0
        newhead=ListNode(0)
        newhead.next=head
        ans=newhead
        while head!=None:
            llen+=1
            head=head.next
        # print llen
        s=llen-n
        while nllen!=s:
            nllen+=1
            newhead=newhead.next
        newhead.next= newhead.next.next
        return ans.next
if __name__ == '__main__':
    ll=ListNode(0)
    head=ll
    # print type(ll)
    # print type(head)
    llist=[1,2,3,4,5,6]
    for i in llist:
        # print i
        ll.next=ListNode(i)
        ll=ll.next
        # print ll.val
    head=head.next
    # while head!=None:
    #     print head.val
    #     head=head.next
    ans=Solution().removeNthFromEnd(head, 3)
    print ans
    while ans!=None:
        print ans.val
        ans=ans.next