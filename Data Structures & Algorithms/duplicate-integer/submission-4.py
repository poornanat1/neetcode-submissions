class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        for i, x in enumerate(nums):
            if x in hashmap.keys():
                return True
            else:
                hashmap[x]=i
        return False