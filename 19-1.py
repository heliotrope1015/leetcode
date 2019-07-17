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
        p=head
        q=head
        while n>0:
            if q.next!=None:
                q = q.next
                n -= 1
            else:
                return head.next
        while q.next!=None:
            q=q.next
            p=p.next
        p.next=p.next.next
        return head
if __name__ == '__main__':
    ll=ListNode(0)
    head=ll
    # print type(ll)
    # print type(head)
    llist=[1]
    for i in llist:
        # print i
        ll.next=ListNode(i)
        ll=ll.next
        # print ll.val
    head=head.next
    # while head!=None:
    #     print head.val
    #     head=head.next
    ans=Solution().removeNthFromEnd(head, 1)
    print ans
    while ans!=None:
        print ans.val
        ans=ans.next