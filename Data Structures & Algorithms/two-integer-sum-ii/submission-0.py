class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        max_index = len(numbers) - 1

        index1 = 0
        index2 = max_index

        while (numbers[index1] + numbers[index2]) != target:
            if numbers[index1] + numbers[index2] < target:
                index1 += 1
            if numbers[index1] + numbers[index2] > target:
                index2 -= 1
        
        return [index1 + 1, index2 + 1]
        