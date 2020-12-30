from recursive_traversal import order_recu_return
class TreeNode:
    def __init__(self, x=None, lchild=None, rchild=None):
        self.val = x
        self.left = lchild
        self.right = rchild


def pre_order_non_recu(root):
    if not root:
        return []
    stack, res = [], []
    while stack or root:
        if root:
            stack.append(root)
            res.append(root.val)
            root = root.left
        else:
            root = stack.pop()
            root = root.right
    return res


def in_order_non_recu(root):
    if not root:
        return []
    stack, res = [], []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            res.append(root.val)
            root = root.right
    return res


def post_order_non_recu(root):
    if not root:
        return []
    stack1, stack2 = [root], []
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)
    res = []
    while stack2:
        res.append(stack2.pop().val)
    return res


def pre_order_non_color(root):
    white, gray, res = 0, 1, []
    stack = [(white, root)]
    while stack:
        color, node = stack.pop()
        if not node:
            continue
        if color == white:
            stack.append((white, node.right))
            stack.append((white, node.left))
            stack.append((gray, node))
        else:
            res.append(node.val)
    return res


def in_order_non_color(root):
    white, gray, res = 0, 1, []
    stack = [(white, root)]
    while stack:
        color, node = stack.pop()
        if not node:
            continue
        if color == white:
            stack.append((white, node.right))
            stack.append((gray, node))
            stack.append((white, node.left))
        else:
            res.append(node.val)
    return res


def post_order_non_color(root):
    white, gray, res = 0, 1, []
    stack = [(white, root)]
    while stack:
        color, node = stack.pop()
        if not node:
            continue
        if color == white:
            stack.append((gray, node))
            stack.append((white, node.right))
            stack.append((white, node.left))
        else:
            res.append(node.val)
    return res



if __name__ == "__main__":
    tree_root = TreeNode(x=1,
                         lchild=TreeNode(x=2, lchild=TreeNode(x=4,
                                                              rchild=TreeNode(7))),
                         rchild=TreeNode(x=3, lchild=TreeNode(5), rchild=TreeNode(6)))
    print('*'*20)
    print("pre_order_recu")
    print('target: %s' % order_recu_return(tree_root, way='pre'))
    print('stack: %s' % pre_order_non_recu(tree_root))
    print('color: %s' % pre_order_non_color(tree_root))

    print('*' * 20)
    print("in_order_recu")
    print('target: %s' % order_recu_return(tree_root, way='in'))
    print('stack: %s' % in_order_non_recu(tree_root))
    print('color: %s' % in_order_non_color(tree_root))

    print('*' * 20)
    print("post_order_recu")
    print('target: %s' % order_recu_return(tree_root, way='post'))
    print('stack: %s' % post_order_non_recu(tree_root))
    print('color: %s' % post_order_non_color(tree_root))