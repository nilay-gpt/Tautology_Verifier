#!/usr/bin/env python


class TreeNode(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        # return "[{}:{}:{}]".format(self.left, self.data, self.right)
        return " " + str(self.data) + " "

    def in_traversal(self):
        if self.left:
            self.left.in_traversal()
        # print(self, end=' ')
        if self.right:
            self.right.in_traversal()


# main
if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.in_traversal()
