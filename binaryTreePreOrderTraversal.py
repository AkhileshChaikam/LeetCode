__author__ = 'KH9057'
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        List1 = []
        List2 = []
        if(root):
           top = self.push(List1,root)
           self.push(List2,root.val)
        while(not self.isEmpty(List1)):
            while(List1[top].left):
                self.push(List2,List1[top].left.val)
                top = self.push(List1,List1[top].left)
                List1[top-1].left = None
            temp = List1.pop()
            top -= 1
            if(temp.right):
                self.push(List2,temp.right.val)
                top = self.push(List1,temp.right)
        return List2

    def push(self,List1,obj):
        List1.append(obj)
        return len(List1) - 1

    def isEmpty(self,List1):
        if(len(List1) is 0):
            return True
        else:
            return False

n= TreeNode(1)
n2= TreeNode(2)
n.right = n2
sol = Solution()
sol.postorderTraversal(n)
