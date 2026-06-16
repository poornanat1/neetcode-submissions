class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, x in enumerate(nums):
            y = target - x
            if y in hashmap.keys():
                result = [i,hashmap[y][0]]
                result.sort()
                return result
            if x not in hashmap.keys():
                hashmap[x]=[i]
            else:
                hashmap[x].append(i)