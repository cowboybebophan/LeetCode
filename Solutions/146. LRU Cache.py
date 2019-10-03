"""
https://leetcode.com/problems/lru-cache/discuss/45952/Python-concise-solution-with-comments-(Using-OrderedDict).

Solution 1 uses OrderedDict(): it is a dictionary subclass that remembers insertion order.
                               Check OrderedDict() here: https://github.com/python/cpython/blob/2.7/Lib/collections.py 

Solutin 2 uses deque: we remove and append back the key(on the right side of the deque) everytime we get(key), making sure that
                      the least recently used key stays on the left-most place of the deque.

"""
# Solution 1

import collections

class LRUCache:

    def __init__(self, capacity):
        self.dict = collections.OrderedDict()     # Using OrderedDict() to remember the order in which the keys were added.
        self.k = capacity
        
    def get(self, key):
        if key not in self.dict:
            return -1
        v = self.dict.pop(key)        # Why don't we just return dict[key] here?
        self.dict[key] = v            # Because then we won't be able to tell which key is the most/least recently used.
        return v                      # Poping and adding back the key/value makes sure that OrderedDict() remembers the order
                                      # so that we can use popitem(last = False) to pop the key that is least recently used.
    def put(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        elif len(self.dict) == self.k:
            self.dict.popitem(last = False) 
        self.dict[key] = value
        
# Solution 2

import collections

class LRUCache:

    def __init__(self, capacity):
        self.deque = collections.deque([])
        self.dic = {}
        self.capacity = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        self.deque.remove(key)
        self.deque.append(key)
        return self.dic[key]

    def put(self, key, value):
        if key in self.dic:    
            self.deque.remove(key)
        elif len(self.dic) == self.capacity:
            v = self.deque.popleft()  # remove the Least Recently Used element
            self.dic.pop(v)
        self.deque.append(key)
        self.dic[key] = value 
