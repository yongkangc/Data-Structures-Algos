package main

import "fmt"

const AlphabetSize = 26

// Node is a node in a trie
type Node struct {
	children [26]*Node
	isEnd    bool
}

// Trie holds the pointer to the root node of the trie
type Trie struct {
	root *Node
}

//Create and Return pointer of the trie
func InitTrie() *Trie {
	result := &Trie{root: &Node{}}
	return result
}

// Insert will take a string and insert it into the trie
func (t *Trie) Insert(s string) {
	wordLength := len(s)
	currentNode := t.root
	for i := 0; i < wordLength; i++ {
		letter := s[i] - 'a' // this changes the base number for letters to start from 0
		// if the letter is not in the index of children then add it
		if currentNode.children[letter] == nil {
			currentNode.children[letter] = &Node{}
		}
		currentNode = currentNode.children[letter]
	}
	currentNode.isEnd = true
}

// Search will take in a word and Return true if the word is in the trie
func (t *Trie) Search(s string) bool {
	wordLength := len(s)
	currentNode := t.root
	for i := 0; i < wordLength; i++ {
		letter := s[i] - 'a' // this changes the base number for letters to start from 0
		// if the letter is not in the index of children then add it
		if currentNode.children[letter] == nil {
			return false
		}
	}
	if currentNode.isEnd == true {

		return true
	}
}

func main() {
	testTrie := InitTrie()
	fmt.Println(testTrie.root)

	toAdd := []string{
		"a",
		"ab",
		"abc",
		"abcd",
		"abcde",
		"abcdef",
		"abcdefg",
		"abcdefgh"
	}
	for _, s := range toAdd {
		testTrie.Insert(s)
	}
	//search
	fmt.Println(testTrie.Search("abcdefgh"))
	// search negative
	fmt.Println(testTrie.Search("abcdefghi"))

}
