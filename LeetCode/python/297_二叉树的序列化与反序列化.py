# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#,'
        s = str(root.val) + ','
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return s + left + right

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        temp = data.split(',')

        def helper(temp_list):
            value = temp_list.pop(0)
            if value == '#':
                return None
            root = TreeNode(value)
            root.left = helper(temp_list)
            root.right = helper(temp_list)
            return root

        return helper(temp)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))