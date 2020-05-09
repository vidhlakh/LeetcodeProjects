import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent = None
        depth = 0
        xdata = []
        ydata = []
        self.dfs(root, x, y, depth, parent, xdata, ydata)

        return xdata[0][0] == ydata[0][0] and xdata[0][1] != ydata[0][1]

    def dfs(self, root, x, y, depth, parent, xdata, ydata):
        if root is None:
            return None
        if root.val == x:
            xdata.append((depth, parent))
        if root.val == y:
            ydata.append((depth, parent))
        self.dfs(root.left, x, y, depth + 1, root, xdata, ydata)
        self.dfs(root.right, x, y, depth + 1, root, xdata, ydata)

n6 = TreeNode(6, None, None)
n5 = TreeNode(5, n6, None)
n4 = TreeNode(4, None, None)
n3 = TreeNode(3, None, n5)
n2 = TreeNode(2, n4, None)
n1 = TreeNode(1, n2, n3)

class Test(unittest.TestCase):
    cases = [
        (1, 2, False),
        (3, 2, False),
        (2, 3, False),
        (4, 3, False),
        (4, 5, True),
        (5, 4, True)
    ]

    def test(self):
        for x, y, expected in self.cases:
            s = Solution()
            result = s.isCousins(n1, x, y)

            self.assertEqual(result, expected)
if __name__=="__main__":
    unittest.main()