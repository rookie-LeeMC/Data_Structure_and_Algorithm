ans = 0


def search(root):
    if not root: ans
    height(root)

    return ans


def height(root):
    if not root: return 0
    L = height(root.left)
    R = height(root.right)

    ans = max(L + R, ans)

    return 1 + max(L, R)
