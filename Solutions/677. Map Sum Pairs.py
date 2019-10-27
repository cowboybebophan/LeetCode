# Brute Force 1     
# Time Complexity: O(N*P) N: number of item in map / P: length of prefix
class MapSum:
    def __init__(self):    
        self.mapSum = {}

    def insert(self, key, val):
        self.mapSum[key] = val
            
    def sum(self, prefix):
        count = 0
        for key in self.mapSum:
            if self.startsWithPrefix(key, prefix):
                count += self.mapSum[key]
        return count            
    
    def startsWithPrefix(self, key, prefix):
        if len(key) >= len(prefix):
            for i in range(len(prefix)):
                if key[i] != prefix[i]:
                    return False
            return True
        return False
    
# Brute Force 2 using str.startswith(prefix)
class MapSum:
    def __init__(self):
        self.mapSum = {}

    def insert(self, key, val):
        self.mapSum[key] = val

    def sum(self, prefix):
        return sum(val for key, val in self.mapSum.items()
                   if key.startswith(prefix))    

# Prefix HashTable
# Insert operation is O(K^2), where K is the length of the key, 
# as K strings are made of an average length of K. Every sum operation is O(1).

class MapSum:
    def __init__(self):
        self.map = {}
        self.count = {}

    def insert(self, key, val):
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        for i in range(len(key)):
            prefix = key[:i+1]
            self.count[prefix] = self.count.get(prefix,0) + diff
            
    def sum(self, prefix):
        return self.count.get(prefix, 0)
    
# Trie
# Time Complexity: Every insert operation is O(K), where K is the length of the key. Every sum operation is O(K).
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class MapSum:
    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += diff
    
    def sum(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count


