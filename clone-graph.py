__author__ = 'KH9057'
"""Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""


# Definition for a undirected graph node
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        dict1 = {}
        if(node):
           return self.cloneGraph1(node,dict1)
        return None

    def cloneGraph1(self,node,dict1):
        Node = UndirectedGraphNode(node.label)
        dict1[node.label] = Node
        for i in node.neighbors:
            if(dict1.get(i.label,"noval") == "noval"):
                Node.neighbors.append(self.cloneGraph1(i,dict1))
            else:
                Node.neighbors.append(dict1.get(i.label,-1))
        return Node
