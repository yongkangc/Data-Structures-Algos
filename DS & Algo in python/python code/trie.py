# there are 2 ways to implement tries. Either with deafault dict or with a dictionary
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currentNode = self.root
        for char in word:
            charIndex = ord(char) - ord("a")
            if not currentNode.child[charIndex]:
                currentNode.child[charIndex] = Node()
            currentNode = currentNode.child[charIndex]
        currentNode.isEnd = True
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currentNode = self.root
        for char in word:
            charIndex = ord(char) - ord("a")
            if not currentNode.child[charIndex]:
                return False
            currentNode = currentNode.child[charIndex]
        return True if currentNode.isEnd == True else False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currentNode = self.root
        for char in prefix:
            charIndex = ord(char) - ord("a")
            if not currentNode.child[charIndex]:
                return False
            currentNode = currentNode.child[charIndex]
        return True

class Node:
    def __init__(self):
        self.child = [None for i in range(26)] 
        self.isEnd = False


# DEFAULT DICT

class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True


# Using Trie to store the words that we can do a lookup when we are traversing the board
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        curr_node = self.root
        
        for char in word:
            if not curr_node.children.get(char):
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        
        curr_node.isWord = True
    
    def search(self,word):
        curr_node = self.root
        
        for char in word:
            if not curr_node.children.get(char):
                return False
                        
            curr_node = curr_node.children.get(char)
            
        return current.isWord