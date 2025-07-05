from typing import List
from collections import deque

class Node:
      def __init__(self, key=None):
            self.key = key
            self.left = None
            self.right = None
            

class BST:
      def __init__(self):
            self.root = None
      def insert(self, key):
            self.root = self._insert(self.root, key)
      def _insert(self, node, key):
            if node is None:
                  return Node(key)
            if key < node.key:
                  node.left = self._insert(node.left, key)
            if key > node.key:
                  node.right = self._insert(node.right, key)
            return node     
      def delete(self, key):
            self.root = self._delete(self.root, key)
      def _delete(self, node, key):
            if node is None:
                  return None
            if key < node.key:
                  node.left = self._delete(node.left, key)
            elif key > node.key:
                  node.right = self._delete(node.right, key)
            else:
                  if node.left is None:
                        return node.right
                  if node.right is None:
                        return node.left
                  
                  inOrderSuccessor = self._findMin(node.right) #find the inorder successor
                  node.key = inOrderSuccessor.key #copy the inorder successor's key to the node
                  node.right = self._delete(node.right, inOrderSuccessor.key) #delete the inorder successor
            return node
      def _findMin(self, node):
            while node.left is not None:
                  node = node.left
            return node     
      def inorder(self):
            self._inorder(self.root)
            print()
      def _inorder(self, node):
            if node is not None:
                  self._inorder(node.left)
                  print(node.key, end=' ')
                  self._inorder(node.right)  
      def preorder(self):
            self._preorder(self.root)
            print()
      def _preorder(self, node):
            if node is not None:
                  print(node.key, end=' ')
                  self._preorder(node.left)
                  self._preorder(node.right)
      def postorder(self):
            self._postorder(self.root)
            print()
      def _postorder(self, node):
            if node is not None:
                  self._postorder(node.left)
                  self._postorder(node.right)
                  print(node.key, end=' ')
      def search(self, key):
            return self._search(self.root, key)
      def _search(self, node, key):
            if node is None :
                  return False
            if node.key == key:
                  return True
            if key < node.key:
                  return self._search(node.left, key)
            else:
                  return self._search(node.right, key)

bst = BST()
bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(10)
bst.insert(14)
bst.insert(13)

print("Inorder Traversal:")
bst.inorder()

print("Preorder Traversal:")
bst.preorder()

print("Postorder Traversal:")
bst.postorder()

print("Search for 6:")
print(bst.search(6)==True)

print("Delete 3:")
bst.delete(3)

