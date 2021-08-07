class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        if not words or not board:
            return
        
        result = []
        
        # build trie
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(trie.root,board,row,col,"",result)
        
        return result
                

    def dfs(self,node,board,row,col,word,result):
        # if word exists, append word to result
        if node.isWord:
            result.append(word)
            node.isWord = False

            
        # return if its out of range
        max_row = len(board)
        max_col = len(board[0])
        
        if row >= max_row or col >= max_col or row <0 or col < 0:
            return
        
        cell = board[row][col]
        
        # if the cell is nothing or visited, return
        if not cell or cell == "#":
            return
                
        node = node.children.get(cell) # update current node

        if not node:         # check if the cell exist in the tree, if exist go down that rabit hole, else return
            return
        
        # append character to word
        word += cell
        
        board[row][col] = '#' # visit the cell

        # traverse to surrounding board
        self.dfs(node,board,row - 1 ,col,word,result)
        self.dfs(node,board,row,col - 1,word,result)
        self.dfs(node,board,row + 1,col,word,result)
        self.dfs(node,board,row,col + 1,word,result)

        board[row][col] = cell # after visiting the surroudning board, return them back to normal
        
                
        
       
        
        
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

        

