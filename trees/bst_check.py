class Solution:
    # do an inorder traversal, then check if the list is sorted and doesnt have any repeated elements
    def isValidBST(self, root) -> bool:
        ans=[]
        def inorder(node):
            if node:
                inorder(node.left)
                ans.append(node.val)
                inorder(node.right)
        inorder(root)
        i = 0
        while i < len(ans)-1:
            if ans[i] >= ans[i+1]:
                return False
            i+= 1
            
        return True
