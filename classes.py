class Node:
    def __init__(self):
        self.parent = None
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()
        self.allWords = []
    
    def insert(self, word):
        curr = self.root
        for i in range(len(word)):
            toInsert = word[i]
            if (toInsert not in curr.children):
                curr.children[toInsert] = Node()
                curr.children[toInsert].parent = curr
            curr = curr.children[toInsert]
        curr.children[""] = None
    
    def endNode(self, word):
        curr = self.root
        for i in range(len(word)):
            toFind = word[i]
            if (toFind not in curr.children):
                return None
            curr = curr.children[toFind]
        if ("" in curr.children):
            return curr
        else:
            return None
    
    def search(self, word):
        return self.endNode(word) != None
    
    def delete(self, word):
        end = self.endNode(word)
        #*Just remove the "" at the end node. 
        if (end!=None):
            del end.children[""]
            print("deleted")
        else:
            print("Doesn't exist")
    
    def startsWithPrefix(self, word):
        curr = self.root
        for i in range(len(word)):
            toFind = word[i]
            if (toFind not in curr.children):
                return False
            curr = curr.children[toFind]

        return True

    def dfs(self, curr, wordSoFar):
        if ("" in curr.children):
            self.arr.append(wordSoFar)
        for key in curr.children:
            if (key!=""):
                self.dfs(curr.children[key], wordSoFar+key)
    
    def display(self):
        self.arr = []
        self.dfs(self.root, "")
        for i in self.arr:
            print(i)

    def suggest(self, word):
        if (self.startsWithPrefix(word)):
            curr = self.root
            for i in range(len(word)):
                curr = curr.children[word[i]]
            self.arr = []
            self.dfs(curr, word)
            for i in self.arr:
                print(i)