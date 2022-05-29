"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    """
    Runtime         48 ms
    Memory usage    14.1 MB

    Runtime: 48 ms, faster than 99.08% of Python3 online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 14.1 MB, less than 14.07% of Python3 online submissions for Longest Substring Without Repeating Characters.
    ---------------------------------------------
    Fastest runtime:    48 ms
    Runtime: 48 ms, faster than 99.08% of Python3 online submissions for Longest Substring Without Repeating Characters.

    Best Memory Usage:  13.9 MB
    Memory Usage: 13.9 MB, less than 99.60% of Python3 online submissions for Longest Substring Without Repeating Characters.

    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        max_length = 0
        for char in s:
            # Try to extend the current substring firstly
            if char not in substring:
                substring += char
                # Try to update max_length
                if (l := len(substring)) > max_length:
                    max_length = l
            else:
                # Since char is in the string
                # we need to move our scope
                # to the first conflicting char
                index = substring.index(char)
                substring = substring[index+1:] + char

        return max_length


# Testing
assert Solution().lengthOfLongestSubstring('aab') == 2
assert Solution().lengthOfLongestSubstring('aabc') == 3
assert Solution().lengthOfLongestSubstring('aabciopa') == 6
assert Solution().lengthOfLongestSubstring('aabciopa') == 6
assert Solution().lengthOfLongestSubstring('abcabcbb') == 3
