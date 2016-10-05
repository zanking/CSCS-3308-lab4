# This class implements a Binary Search Tree Class
# The binary search tree class will include functionality of
#   1. Insert a Node in the Tree.
#   2. Search for a Node in the Tree
#   3. Various traversals including in order, preorder and postorder traversals.
#
#  The binary search tree is made of class Node objects.
#    Each node has three members: key is an integer, left and right child point to nodes.
#    If left is None, then it means that the node has no left child.
#    If right is None then the node has no right child.

# Name: Your Name Here
# On my honor as a University of Colorado Student, this code was entirely written by myself with no unauthorized help.

class Node:

    def __init__(self, my_key): # Constructor for the Node.
        self.key = my_key       # Set the key to my_key
        self.left = None        # Set left child to None
        self.right = None       # Set right child to None

    def insert(self, key_to_insert):
        # TODO: write an insert function for the BST.
        # NOTE: If key_to_insert equals my_key,
        #       then the node need should NOT be inserted in the tree.
        # REMOVE the assert below
        if key_to_insert == self.key:
            return
        elif key_to_insert < self.key:
            if self.left == None:
                self.left = Node(key_to_insert)
            else:
                self.left.insert(key_to_insert)
        else:
            if self.right == None:
                self.right = Node(key_to_insert)
            else:
                self.right.insert(key_to_insert)

    def inorder_traversal(self, ret_list):
        # TODO: write an inorder traversal function for the BST.
        # REMOVE the assert below
        if self.left != None:
            self.left.inorder_traversal(ret_list)
        ret_list.append(self.key)
        if self.right != None:
            self.right.inorder_traversal(ret_list)

    def get_depth(self):
        # TODO: write a get_depth function for the BST
        #   Depth of a tree with no children is 1.
        #   Otherwise, depth = 1 + max(depth(left subtree), depth(right subtree))
        # REMOVE the assert below
        depth = 1
        if self.left != None:
            depth = max(depth, self.left.get_depth() + 1)
        if self.right != None:
            depth = max(depth, self.right.get_depth() + 1)
        return depth
    def key_exists(self, key_to_find):
        # return True if the key_to_find is already in the tree,
        #   otherwise return False
        # REMOVE the assert below
        if key_to_find == self.key:
            return True
        res = False
        if self.left != None:
            res = res or self.left.key_exists(key_to_find)
        if self.right != None:
            res = res or self.right.key_exists(key_to_find)
        return res

if __name__ == '__main__':
    print('Please do not call this file directly.')
    print('To run autograder script: please call the test_bst.py')