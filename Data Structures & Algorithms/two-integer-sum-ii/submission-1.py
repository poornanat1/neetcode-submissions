class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = 0
        while j < len(numbers):
            complement = target - numbers[j]
            if complement in numbers:
                complement_idx = numbers.index(complement)
                if complement_idx != j:
                    return [j+1, complement_idx+1]
            j+=1