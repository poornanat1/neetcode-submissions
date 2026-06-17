class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashmap = dict()
        for i, n in enumerate(nums):
            nums_copy = nums.copy()
            nums_copy.pop(i)
            hashmap[i]=nums_copy
        result = []
        for k,v in hashmap.items():
            product = 1
            for j in v:
                product *= j
            result.append(product)
        return result