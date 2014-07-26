__author__ = 'KH9057'
'''Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.'''

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        sum,sum1=self.maxPathSum1(root)
        return max(sum,sum1)

    def maxPathSum1(self,root):
        if(root is None):
            return -2147483648,-2147483648
        sum,sum1 = self.maxPathSum1(root.left)
        sum2,sum3 = self.maxPathSum1(root.right)
        return max(sum,sum2,sum1+root.val,sum3+root.val,root.val,sum1+sum3+root.val),max(root.val,root.val+sum1,root.val+sum3)