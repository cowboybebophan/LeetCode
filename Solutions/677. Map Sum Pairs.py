# Brute Force
class MapSum:
    def __init__(self):    
        self.mapSum = {}

    def insert(self, key: str, val: int) -> None:
        self.mapSum[key] = val
            
    def sum(self, prefix: str) -> int:
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

# Trie
