# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        inorder = sorted(preorder)
        return self.bstFromPreorderInorder(preorder,inorder)

    def bstFromPreorderInorder(self,preorder,inorder):
        lengthpre = len(preorder)
        lengthin = len(inorder)
        if (lengthpre != lengthin) or preorder == None or inorder == None or lengthpre ==0:
            return None
        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)
        root.left = self.bstFromPreorderInorder(preorder[1:rootindex +1 ], inorder[:rootindex])
        root.right = self.bstFromPreorderInorder(preorder[rootindex+1:], inorder[rootindex+1 :])
        return root
s = Solution()
root = s.bstFromPreorder([8,5,1,7,10,12])
print(root)
