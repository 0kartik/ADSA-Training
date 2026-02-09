def nfl(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    else:
        if root.left is None or root.right is None:
            return nfl(root.left)+nfl(root.right)
        else: 
            return 1+nfl(root.left)+nfl(root.right)