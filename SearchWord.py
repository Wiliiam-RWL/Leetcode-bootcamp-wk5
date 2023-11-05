from typing import List


class Node:
    def __init__(self):
        self.child = {}
        self.end = None  # word


class Tries:
    def __init__(self):
        self.root = Node()

    def inser_word(self, word):
        cur = self.root
        for c in word:
            if c in cur.child:
                cur = cur.child[c]
            else:
                cur.child[c] = Node()
                cur = cur.child[c]
        cur.end = word


class Solution:
    def dfs(self, i, j, node: Node, visited: set, res: list, m, n, board):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if node.end:
            res.append(node.end)
        if not node.child:
            return

        for r, c in directions:
            row, col = i + r, c + j
            if -1 < row and row < m and -1 < col and col < n and (row,col) not in visited and board[row][col] in node.child:
                visited.add((row, col))
                self.dfs(row, col, node.child[board[row][col]], visited, res, m, n, board)
                visited.remove((row, col))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(words), len(words[0])
        visited = set()
        tries = Tries()
        res = []

        for w in words:
            tries.inser_word(w)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in tries.root.child:
                    visited.add((i,j))
                    self.dfs(i,j,tries.root.child[board[i][j]],visited,res,m,n,board)
                    visited.remove((i,j))
        
        return list(set(res))
