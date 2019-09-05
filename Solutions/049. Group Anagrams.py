"""
First, we creat a empty dictionary to store the answers:
keys are the elements of the strings, values are the anagrams. 

The tuple function gets the strings' components: tuple("aab") = ("a","a","b");
We used the sorted function to make sure that anagrams like "aab" and "baa" are sorted into the same key ("a","a","b");
Otherwise, "aab" and "baa" will be two different keys.

Then we update the value of a certain key if the string we are going through right now is of the same key.
Be careful here: instead of simply using d.get(key), we use d.get(key,[]) here.

When get() is called, Python checks if the specified key exists in the dict. 
If it does, then get() returns the value of that key. 
If the key does not exist, then get() returns the value specified in the second argument to get().

"""

class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for s in strs:
            key = tuple(sorted(s))
            d[key] = d.get(key,[]) + [s]
        return list(d.values())
        
