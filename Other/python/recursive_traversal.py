class TreeNode:
    def __init__(self, x=None, lchild=None, rchild=None):
        self.val = x
        self.left = lchild
        self.right = rchild


def pre_order_recu(root):
    if not root:
        return
    print(root.val, end=' ')
    pre_order_recu(root.left)
    pre_order_recu(root.right)


def in_order_recu(root):
    if not root:
        return
    in_order_recu(root.left)
    print(root.val, end=' ')
    in_order_recu(root.right)


def post_order_recu(root):
    if not root:
        return
    post_order_recu(root.left)
    post_order_recu(root.right)
    print(root.val, end=' ')


def order_recu_return(root, way):
    if not root:
        return []
    left = order_recu_return(root.left, way)
    right = order_recu_return(root.right, way)
    if way == 'pre':
        return [root.val]+left+right
    elif way == 'in':
        return left+[root.val]+right
    elif way == 'post':
        return left+right+[root.val]
    else:
        raise ValueError('way is wrong: only pre, in, post')


def level_order(root):
    if not root:
        return
    stack = [root]
    res = []
    while stack:
        node = stack.pop(0)
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res


if __name__ == "__main__":
    tree_root = TreeNode(x=1,
                         lchild=TreeNode(x=2, lchild=TreeNode(x=4,
                                                              rchild=TreeNode(7))),
                         rchild=TreeNode(x=3, lchild=TreeNode(5), rchild=TreeNode(6)))
    print('*'*20)
    print("pre_order_recu")
    pre_order_recu(tree_root)
    print(order_recu_return(tree_root, 'pre'))

    print('*' * 20)
    print("in_order_recu")
    in_order_recu(tree_root)
    print(order_recu_return(tree_root, 'in'))

    print('*' * 20)
    print("post_order_recu")
    post_order_recu(tree_root)
    print(order_recu_return(tree_root, 'post'))

    print('*' * 20)
    print("level_order")
    print(level_order(tree_root))