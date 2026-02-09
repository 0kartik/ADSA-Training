def nnl(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    else:
        return 1+nnl(root.left)+nnl(root.right)