"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Picture

(2) --> (4) --> (3)
(5) --> (6) --> (4)

___________________
(7) --> (0) --> (8)


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime         75 ms
    Memory usage    13.9 MB

    # Description is from the second run.
    Runtime: 80 ms, faster than 66.42% of Python3 online submissions for Add Two Numbers.
    Memory Usage: 13.8 MB, less than 86.85% of Python3 online submissions for Add Two Numbers.
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = f'{l1.val}'
        node_1 = l1
        while (node_1 := node_1.next) is not None:
            l1_num += str(node_1.val)
        l2_num = f'{l2.val}'
        node_2 = l2
        while (node_2 := node_2.next) is not None:
            l2_num += str(node_2.val)
        res_num_str = str(int(l1_num[::-1]) + int(l2_num[::-1]))
        previous, current = None, None
        for el in res_num_str:
            num = int(el)
            current = ListNode(val=num)
            if previous is not None:
                current.next = previous
            previous = current
        return current


class SolutionImproved:
    """
    Runtime         71 ms
    Memory usage    13.8 MB

    Runtime: 71 ms, faster than 85.24% of Python3 online submissions for Add Two Numbers.
    Memory Usage: 13.8 MB, less than 86.81% of Python3 online submissions for Add Two Numbers.

    Fastest runtime:    64 ms
    Best Memory Usage:  13.8 MB
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1, list2 = l1, l2
        extra = 0
        node, previous = None, None
        while list1 or list2:
            summary = getattr(list1, 'val', 0) + getattr(list2, 'val', 0) + extra
            val = summary % 10
            extra = summary // 10
            current = ListNode(val=val)
            # Save the beginning
            if node is None:
                node = current
            if previous:
                # Set current node as next for the previous node
                previous.next = current
            # Move to the next node
            previous = current
            list1, list2 = getattr(list1, 'next', None), getattr(list2, 'next', None)
        else:
            # Check if extra left
            # Ex. leading 10 (1).
            if extra:
                current = ListNode(val=extra)
                previous.next = current

        return node
