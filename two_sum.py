# rewrite this solution. it kind of sucks.

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
assert([0, 1] == s.twoSum([2,7,11,15], 9))
assert([0, 4] == s.twoSum([2,7,11,15, 2], 4))
assert([0, 1] == s.twoSum([3,3], 6))


# def twoSumNotDistinct(self, nums: list[int], target: int) -> list[int]:
#     # going to have index and num
#     num_to_indexes = {}
#     for i, num in enumerate(nums):
#         num_to_indexes.setdefault(num, []).append(i)

#     for num in num_to_indexes.keys():
#         num_index = num_to_indexes[num][0]
#         other_num = target - num
#         # special case for equality
#         if other_num == num and len(num_to_indexes[num]) > 1:
#             other_num_index = num_to_indexes[num][1]
#             if other_num_index != num_index:
#                 return [num_index, other_num_index]
#         elif other_num in num_to_indexes:
#             return sorted([num_index, num_to_indexes[other_num][0]])
#     return []
