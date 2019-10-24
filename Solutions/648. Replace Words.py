# Brute Force

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        dict = set(dict)
        
        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in dict:
                    return word[:i]
            return word
        
        return " ".join(map(replace, sentence.split()))
        
# Trie(Prefix Tree / KeyWord Tree)

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True
        
    def find_prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            prefix += char
            if char not in node.children:
                return word
            elif node.children[char].word:
                return prefix
            else:
                node = node.children[char]
        return word
    
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        dict = set(dict)
        trie = Trie()
        words = []
        
        for i in dict:
            trie.insert(i)  
        
        for word in sentence.split():
            words.append(trie.find_prefix(word))
            
        return " ".join(words)
