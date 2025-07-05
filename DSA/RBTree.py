class Node:
      def __init__(self, key, color='R'):
            self.key = key
            self.color = color
            self.left = None
            self.right = None
            self.parent = None
class RedBlackTree:
      def __init__(self):
            self.root = None
      def leftRotate(self, x):
            y = x.right
            x.right  = y.left
            if y.left is not None:
                  y.left.parent = x
            y.parent = x.parent

            if x.parent is None:
                  self.root = y
            elif x == x.parent.left:
                  x.parent.left = y  #If x is the left child of its parent, make y the left child
            else:
                  x.parent.right = y  #If x is the right child of its parent, make y the right child

            y.left = x
            x.parent = y
      def rightRotate(self, x):
            y = x.left
            x.left = y.right
            if y.right is not None:
                  y.right.parent = x
            y.parent = x.parent
            if x.parent is None:
                  self.root = y
            elif x == x.parent.right:
                  x.parent.right = y
            else:
                  x.parent.left = y
            y.right = x
            x.parent = y
      def insert(self,key):
            node  = Node(key)

            y = None
            x = self.root
            while x is not None:
                  y = x
                  if node.key < x.key:
                        x = x.left
                  else:
                        x = x.right

            node.parent = y
            if y is None:
                  self.root = node
            elif node.key < y.key:
                  y.left = node
            else:
                  y.right = node
            
            if node.parent is None:
                  node.color = 'B'
                  return
            if node.parent.parent is None:
                  return
            
            self.fixInsert(node)
      def fixInsert(self, k):
            while k.parent and k.parent.color == 'R':
                  if k.parent == k.parent.parent.left:
                        uncle = k.parent.parent.right
                        if uncle and uncle.color == 'R':
                              uncle.color = 'B'
                              k.parent.color = 'B'
                              k.parent.parent.color = 'R'
                              k = k.parent.parent
                        else:
                              if k == k.parent.right:
                                    k = k.parent
                                    self.leftRotate(k)
                              k.parent.color = 'B'
                              k.parent.parent.color = 'R'
                              self.rightRotate(k.parent.parent)
                  else:
                        uncle = k.parent.parent.left
                        if uncle and uncle.color == 'R':
                              uncle.color = 'B'
                              k.parent.color = 'B'
                              k.parent.parent.color = 'R'
                              k = k.parent.parent
                        else:
                              if k == k.parent.left:
                                    k = k.parent
                                    self.rightRotate(k)
                              k.parent.color = 'B'
                              k.parent.parent.color = 'R'
                              self.leftRotate(k.parent.parent)
                  self.root.color = 'B'