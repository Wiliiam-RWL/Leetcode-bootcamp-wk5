# Definition for a binary tree node.
from ast import List
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = deque()
        if root is None:
            return []
        nodes.append((root, 0))
        res = []
        while nodes:
            now_node, height = nodes.popleft()
            if len(res) - 1 < height:
                res.append([])
            res[height].append(now_node.val)
            if now_node.left is not None:
                nodes.append((now_node.left, height + 1))
            if now_node.right is not None:
                nodes.append((now_node.right, height + 1))
        return res
