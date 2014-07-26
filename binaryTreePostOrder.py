__author__ = 'KH9057'
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        List1 = []
        List2 = []
        if(root):
           top = self.push(List1,root)
        while(not self.isEmpty(List1)):
            while(List1[top].left):
                top = self.push(List1,List1[top].left)
                List1[top-1].left = None
            if(List1[top].right):
                top = self.push(List1,List1[top].right)
                List1[top-1].right = None
            else:
                List2.append(List1.pop().val)
                top -= 1
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
