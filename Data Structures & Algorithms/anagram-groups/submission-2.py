class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in hashmap.keys():
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s]=[s]
        result = []
        for k, v in hashmap.items():
            result.append(v)
        return result