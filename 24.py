# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        # if head.next==None:
        #     return head
        # start=ListNode(0)
        # result=ListNode(0)
        # start.next=head
        # result.next=start.next.next
        new=ListNode(0)
        result=ListNode(0)
        result.next=head
        start=result
        while start.next!=None and start.next.next!=None :
            new.next = start.next.next.next
            start.next.next.next=start.next
            start.next=start.next.next
            start.next.next.next=new.next
            start=start.next.next
        return result.next