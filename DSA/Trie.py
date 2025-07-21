class Node:
    def __init__(self):
        self.links = [None] * 26 
        self.flag = False
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None
    def put(self, ch, node):
        self.links[ord(ch)-ord('a')]=node
    def get(self, ch):
        return self.links[ord(ch)-ord('a')]
    def setEnd(self):
        self.flag=True
    def isEnd(self):
        return self.flag

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i], Node())
            node = node.get(word[i])
        node.setEnd()
       
    def search(self, word):
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                return False
            node = node.get(word[i])
        return node.isEnd()
    def startsWith(self,prefix):
        node = self.root
        for i in range(len(prefix)): 
            if not node.containsKey(prefix[i]):
                return False
            node = node.get(prefix[i])
        return True