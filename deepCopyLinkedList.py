__author__ = 'KH9057'
# Definition for singly-linked list with a random pointer.
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        head1= head
        randomList =None
        if(not head):
            return None
        while(head):
            Node = RandomListNode(head.label)
            Node.next = head.next
            head.next= Node
            head = Node.next
        randomList = head1.next
        head=head1
        while(head and head.next):
            if(head.random):
                head.next.random = head.random.next
            else:
                head.next.random = None
            head = head.next.next
        head = head1
        while(head):
            temp = head.next
            if(temp):
                head.next=temp.next
            head = temp
        return randomList
s=Solution()
Node1 = RandomListNode(-1)
Node2 = RandomListNode(-1)
Node1.next = Node2
Node3= s.copyRandomList(Node1)
while(Node3):
    print Node3.label
    Node3= Node3.random