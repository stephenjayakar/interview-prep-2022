class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            num_to_index.setdefault(num, []).append(i)
        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in num_to_index:
                for other_num_index in num_to_index[other_num]:
                    if other_num_index == i:
                        continue
                    return [i, other_num_index]
        return []

    def twoSumOneIteration(self, nums: list[int], target: int) -> tuple[int, int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in num_to_index:
                return i, num_to_index[other_num]
            num_to_index[num] = i
        return (-1, -1)

s = Solution()
method = s.twoSumOneIteration
assert([0, 1] == sorted(method([2,7,11,15], 9)))
assert([0, 4] == sorted(method([2,7,11,15, 2], 4)))
assert([0, 1] == sorted(method([3,3], 6)))


