def noOfLeaf(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return noOfLeaf(root.left)+noOfLeaf(root.right)