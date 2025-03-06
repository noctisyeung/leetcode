#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited_map = {}
        
        def depth_first_search(node: Optional['Node']):
            if node in visited_map:
                return visited_map[node]
            new_node = Node(node.val)
            visited_map[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(depth_first_search(neighbor))
            return new_node

        return depth_first_search(node) if node is not None else None

        
# @lc code=end

