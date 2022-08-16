// https://leetcode.com/problems/replace-words

class TreeNode:
    
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = ""

class Trie: 
    
    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None: 
        cur = self.root
        for char in word: 
            if char not in cur.children: 
                cur.children[char] = TreeNode()
            cur = cur.children[char]
        cur.isWord = True
        cur.word = word
        return 
    
    def search(self, word: str) -> str: 
        cur = self.root
        for char in word: 
            if cur.isWord: 
                return cur.word
            if char not in cur.children: 
                return word
            cur = cur.children[char]
        return word
    
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary: 
            trie.insert(word)
        ans = []
        for word in sentence.split(' '): 
            ans.append(trie.search(word))
        return ' '.join(ans)