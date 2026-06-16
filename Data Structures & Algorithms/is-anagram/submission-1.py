class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = dict()
        t_hash = dict()
        def fill_hash(strs: str, hashmap: dict):
            for i,x in enumerate(strs):
                if x not in hashmap.keys():
                    hashmap[x]=0
                hashmap[x]+=1
            return hashmap
        s_hash = fill_hash(s, s_hash)
        t_hash = fill_hash(t, t_hash)
        return s_hash == t_hash
