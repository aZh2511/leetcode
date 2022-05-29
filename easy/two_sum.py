"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List


class SolutionLoops:
    """
    Runtime         6472 ms
    Memory usage    14.9 MB
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            num_i = nums[i]
            for k in range(1, length - i):
                k_index = i + k
                num_k = nums[k_index]
                if num_k + num_i == target:
                    return [i, k_index]


class SolutionHashMap:
    """
    Runtime         118 ms
    Memory usage    15.1 MB
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        length = len(nums)
        for i in range(length):
            current = nums[i]
            required = target - current
            if (r_index := hashmap.get(required)) is not None:
                return [i, r_index]
            hashmap[current] = i


class SolutionHashMapImproved:
    """
    Runtime         110 ms
    Memory usage    15.2 MB
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, current in enumerate(nums):
            required = target - current
            if (r_index := seen.get(required)) is not None:
                return [i, r_index]
            seen[current] = i


a = SolutionHashMap().twoSum([2,7,11,15], 9)
print(a)
