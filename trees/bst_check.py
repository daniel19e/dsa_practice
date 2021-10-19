tree_vals=[]
tree=input()
# 1st solution, check if the inorder traversal is equal to all the nodes sorted
def inorder(tree):
    if tree:
        inorder(tree.left)
        tree_vals.append(tree.val)
        inorder(tree.right)

def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)

inorder(tree)
sort_check(tree_vals)

