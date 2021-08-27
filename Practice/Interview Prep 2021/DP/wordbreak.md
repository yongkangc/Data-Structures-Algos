1. [DP](#DP)
    1. [Bottom Up](#bottom-up)
    2. [Cache](#Cache)
2. [Trie](#Trie)
3. [DP+Trie](#DP+Trie)

## DP

### Bottom Up
start to end
- we create a cache to store whether at each index, could we have found a word or not
The idea is the following:

d is an cache that contains booleans

d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

Example:

s = "leetcode"

words = ["leet", "code"]

d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

The result is the last index of d.
```python
def word_break(s, words):
 	d = [False] * len(s)    
 	for i in range(len(s)):
 		for w in words:
 			if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
 				d[i] = True
 	return d[-1]
```

end to start
- base case is the end of the string. If we get to the length of the string, we return true.
- for each index, we see if we start from that index to the end, would we be able to get a word in the word dict?

Recursive relation:
`dp[i] = dp[i + len(word)]`

```python
class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1) # +1 = base case
        dp[len(s)] = True # base case : out of length of base case 
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict: # for each position i, we want to see if there is a word match
                if (i + len(w) <= len(s)) and (s[i:i + len(w)] == w): # check num of characters is enough and checking the word if they are exactly equal
                    dp[i] =  dp[i + len(w)] # recursive relation
                if dp[i]:
                    break
        return dp[0]
# https://www.youtube.com/watch?v=Sx9NNgInc3A&ab_channel=NeetCode
```




## Trie:
- faced some issues with just using trie as it was not able to pass all test cases

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        isWord = True
        trie = Trie()
        
        for word in wordDict:
            trie.insert(word)
        
        return trie.checkString(s)
            
    
class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        curr_node = self.root
        
        for i in word:
            if not curr_node.children.get(i):
                curr_node.children[i] = Node()
            curr_node = curr_node.children[i]
        curr_node.isEnd = True            
    
    def checkString(self,s):
        curr_node = self.root

        for i in range(len(s)):
            if curr_node.isEnd:
                if not curr_node.children.get(s[i+1]).isEnd: # and the next is not end
                    curr_node = self.root
                
            if not curr_node.children.get(s[i]):
                return False
            
            curr_node = curr_node.children[s[i]
            
        
        return curr_node.isEnd
```
### DP+Trie
- Store all the dictionary words inverted in a trie. At stage i of the DP, start traversing the trie for each letter coming behind i and find out all indices where you get an end of word symbol and call DP on those indices.