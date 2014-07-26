__author__ = 'KH9057'
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if(head == None or head.next == None):
            return head
        return self.divideList(head,head,head)

    def divideList(self,head,slow,fast):
        if(head ==None or head.next is None):
            return head
        prev = slow
        while(fast is not None and fast.next is not None):
            prev= slow
            slow = slow.next
            fast = fast.next.next
        prev.next =None
        fast = slow
        slow = self.divideList(head,head,head)
        fast = self.divideList(fast,fast,fast)
        if(slow.val < fast.val):
            result = slow
            slow = slow.next
        else:
            result =fast
            fast = fast.next
        result1=result
        while(slow and fast):
            if(slow.val < fast.val):
                result.next = slow
                result = slow
                slow=slow.next
            elif(slow.val >= fast.val):
                result.next = fast
                result = fast
                fast = fast.next
        while(slow):
            result.next = slow
            result = slow
            slow=slow.next
        while(fast):
             result.next = fast
             result = fast
             fast = fast.next
        return result1


n1 = ListNode(7)
n2 = ListNode(6)
#n3 = ListNode(3)
##n4 = ListNode(5)
##n5 = ListNode(2)
#n6 = ListNode(1)
n1.next = n2
#n2.next = n3
#n3.next = n4
#n4.next = n5
#n5.next = n6
obj = Solution()
temp = obj.sortList(n1)
while(temp):
    print temp.val
    temp = temp.next