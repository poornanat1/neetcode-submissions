class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for n in nums:
            if n in hashmap:
                hashmap[n]+=1
            else:
                hashmap[n]=1
        top_k = sorted(list(hashmap.values()))
        top_k = top_k[-k:]
        result = []
        for i, n in hashmap.items():
            if n in top_k:
                result.append(i)
        return result

        