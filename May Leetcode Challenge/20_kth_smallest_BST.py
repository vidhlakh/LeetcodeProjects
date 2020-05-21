# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):

            if root is None:
                return []
            while(root):
                in_left = inorder(root.left)
                in_val = [root.val]
                in_right = inorder(root.right)
                print("left,val,right:",in_left+in_val+in_right)
                return in_left+in_val+in_right

        return inorder(root)[k-1]



    def insert(self, root,data):
        # print("type of root ",type(self.root))
        #
        # current = self.root
        # print("type of current ", type(current),current.val)
        #
        # while(current):
        #     if new_value < current.val:
        #         current = current.left
        #     else:
        #         current = current.right
        # current = TreeNode(new_value)
        # self.root = current

        if root == None:
            return TreeNode(data)
        else:
            if data <= root.val:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

if __name__=="__main__":
    s = Solution()
    root =TreeNode(7)
    root =s.insert(root,2)
    root =s.insert(root,3)
    root =s.insert(root,5)
    kth_smallest_element = s.kthSmallest(root,1)
    print("Kth smallest element in BST:",kth_smallest_element)

