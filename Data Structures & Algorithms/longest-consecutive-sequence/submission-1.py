class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            streak=1
            i = n
            if n-1 not in num_set:
                while i+1 in num_set:
                    streak+=1
                    i+=1
                longest = max(longest, streak)
                
        return longest