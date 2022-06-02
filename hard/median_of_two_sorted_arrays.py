"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from typing import List


# todo: check the length and just store median numbers


class Solution:
    """
    Runtime         177 ms
    Memory usage    14.2 MB

    Runtime: 177 ms, faster than 16.79% of Python3 online submissions for Median of Two Sorted Arrays.
    Memory Usage: 14.2 MB, less than 67.97% of Python3 online submissions for Median of Two Sorted Arrays.
    ---------------------------------------------
    Fastest runtime:    129 ms
    Runtime: 129 ms, faster than 48.79% of Python3 online submissions for Median of Two Sorted Arrays.

    Best Memory Usage:  14 MB
    Memory Usage: 14 MB, less than 99.68% of Python3 online submissions for Median of Two Sorted Arrays.
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        That could be useful if we did not know the length of the upcoming data.
        """
        # median numbers
        nums = []
        # Upcoming numbers
        next_nums = []
        is_odd = False

        def add_num(num: int):
            """
            store median numbers and upcoming numbers

            :param num: next number of the final array.
            :return: None
            """
            nonlocal nums, is_odd
            is_odd = not is_odd

            if not nums:
                nums.append(num)
                return
            if not is_odd:
                if next_nums:
                    nums.append(next_nums.pop(0))
                    next_nums.append(num)
                else:
                    nums.append(num)
            else:
                nums = [nums[1]]
                next_nums.append(num)

        i, k = 0, 0
        len_i, len_k = len(nums1), len(nums2)
        while True:
            # Break cycle condition is going through two lists.
            # But the lists might be of different length.
            # Also, in that way we handle the case, when we reach
            # the end of only one of the lists.
            if i == len_i:
                for el in nums2[k:]:
                    add_num(el)
                break
            elif k == len_k:
                for el in nums1[i:]:
                    add_num(el)
                break
            num_i = nums1[i]
            num_k = nums2[k]
            if num_i < num_k:
                i += 1
                add_num(num_i)
            elif num_i > num_k:
                k += 1
                add_num(num_k)
            else:
                i += 1
                k += 1
                add_num(num_i)
                add_num(num_k)
        return sum(nums) / len(nums)


assert Solution().findMedianSortedArrays([1, 2, 3, 300], [2, 7, 8, 9]) == 5
assert Solution().findMedianSortedArrays([1, 2, 3, 300], [2, 7, 8, 9, 10]) == 7


class SolutionTwo:
    """
    Runtime         99 ms
    Memory usage    14.3 MB

    Runtime: 99 ms, faster than 84.49% of Python3 online submissions for Median of Two Sorted Arrays.
    Memory Usage: 14.3 MB, less than 25.00% of Python3 online submissions for Median of Two Sorted Arrays.
    ---------------------------------------------
    Fastest runtime:    94 ms
    Runtime: 94 ms, faster than 91.96% of Python3 online submissions for Median of Two Sorted Arrays.

    Best Memory Usage:  14.2 MB
    Memory Usage: 14.2 MB, less than 25.00% of Python3 online submissions for Median of Two Sorted Arrays.

    Todo: minimize working vars and checks. get array items only when we reach the median.
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        We do not keep in memory anything.
        """
        i, k = 0, 0
        len_i, len_k = len(nums1), len(nums2)
        total_length = len_i + len_k
        is_odd = total_length % 2
        summary = 0
        median = None

        def add_num(num: int):
            nonlocal summary, median, i, k
            counter = i + k
            if is_odd and counter == (total_length // 2) + 1:
                return num
            elif not is_odd and counter == (total_length // 2):
                summary += num
            elif not is_odd and counter == (total_length // 2) + 1:
                return (summary + num) / 2

        for _ in range(total_length):
            if i == len_i:
                for el in nums2[k:]:
                    k += 1
                    median = add_num(el)
                    if median is not None:
                        return median
            elif k == len_k:
                for el in nums1[i:]:
                    i += 1
                    median = add_num(el)
                    if median is not None:
                        return median
            num_i = nums1[i]
            num_k = nums2[k]
            if num_i < num_k:
                i += 1
                median = add_num(num_i)
                if median is not None:
                    return median
            elif num_i > num_k:
                k += 1
                median = add_num(num_k)
                if median is not None:
                    return median
            else:
                i += 1
                median = add_num(num_i)
                if median is not None:
                    return median

                k += 1
                median = add_num(num_k)
                if median is not None:
                    return median

        return median


assert SolutionTwo().findMedianSortedArrays([1, 2, 3, 300], [2, 7, 8, 9]) == 5
assert SolutionTwo().findMedianSortedArrays([1, 2, 3, 300], [2, 7, 8, 9, 10]) == 7
assert SolutionTwo().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert SolutionTwo().findMedianSortedArrays([0, 0], [0, 0]) == 0
