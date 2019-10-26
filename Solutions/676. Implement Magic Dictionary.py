# Trie
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dict: List[str]) -> None:
        for word in dict:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = True
            
    def search(self, word: str) -> bool:
        def dfs(word, count, root):
            if count > 1 or not word:
                return count == 1 and root.word
            return any([dfs(word[1:], count+(word[0]!=c), root.children[c]) for c in root.children])
            
# Brute Force
# Call two strings neighbors if exactly one character can be changed in one 
# to make the strings equal (ie. their hamming distance is 1.)

# Strings can only be neighbors if their lengths are equal. 
# When searching a new word, let's check only the words that are the same length.

class MagicDictionary:
    def __init__(self):
        self.memo = collections.defaultdict(list)

    def buildDict(self, dict: List[str]) -> None:
        for word in dict:
            self.memo[len(word)].append(word)
        
    def search(self, word: str) -> bool:
        return any([sum(a!=b for a,b in zip(word, candidate)) == 1 for candidate in self.memo[len(word)]])
