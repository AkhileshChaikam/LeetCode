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
        return self.insertionSortList(head)

    def insertionSortList(self, head):
        if(head ==None or head.next is None):
            return head
        head1 = head
        head1 = head1.next
        boolean = False
        returnNode =prev = head
        while(head1):
            temp = head1.next
            if(head1.next is None):
                boolean = True
            if(prev.val < head1.val):
                prev=head1
            if(returnNode.val > head1.val):
                returnNode = head1
            head = self.placeTheNode(head1,head,boolean,prev)
            head1 = temp
        return returnNode

    def placeTheNode(self,obj,head,boolean,lastNode):
        prev = None
        head1 = head
        while(head and obj.val > head.val):
            prev = head
            head = head.next
        if(obj is not head):
            temp = obj.next
            obj.next = head
            while(head.next != obj):
                head =head.next
            head.next =temp
            if(prev is not None):
                prev.next = obj
            else:
                return obj
            if(boolean == True):
                lastNode.next = None
        return head1

n1 = ListNode(9)
n2 = ListNode(8)
n3 = ListNode(9)
n4 = ListNode(7)
n5 = ListNode(9)
n6 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
obj = Solution()
temp = obj.sortList(n1)
while(temp):
    print temp.val
    temp = temp.next