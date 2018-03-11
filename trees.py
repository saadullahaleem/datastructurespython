class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.parent = None
        self.left_node = None
        self.right_node = None

    def add_node(self, value):
        if type(value) is not BinaryTree:
            raise ValueError("Node must be of instance BinaryTree")

        if value > self and self.right_node:
            self.right_node.add_node(value)
        elif value > self and not self.right_node:
            self.right_node = value
        elif value < self and self.left_node:
            self.left_node.add_node(value)
        else:
            self.left_node = value

        value.parent = self

    def __gt__(self, other):
        return self.root > other.root

    def traverse_in_order(self):
        # if left node, apply traverse to node
        if self.left_node:
            self.left_node.traverse_in_order()
        print(self, end=' ')
        if self.right_node:
            self.right_node.traverse_in_order()

    def traverse_pre_order(self):
        # if left node, apply traverse to node
        print(self, end=' ')
        if self.left_node:
            self.left_node.traverse_pre_order()
        if self.right_node:
            self.right_node.traverse_pre_order()

    def traverse_post_order(self):
        # if left node, apply traverse to node
        if self.left_node:
            self.left_node.traverse_post_order()
        if self.right_node:
            self.right_node.traverse_post_order()
        print(self, end=' ')

    def __str__(self):
        return str(self.root)