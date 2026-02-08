
"""
Given a string `s`,
find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s: str) -> tuple[int, str]:
    """
    Time complexity: O(n)
    Space complexity: O(min(m, n)), where m is the size of the charset, and n is the size of the string.
    """
    char_index = {}
    longest = 0
    left = 0
    start = 0
    
 

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        if right - left + 1 > longest:
            longest = right - left + 1
            start = left
    return longest, s[start:start+longest]

# Example usage:
s = "bbbbb"
length, substring = lengthOfLongestSubstring(s)
print(f"Length: {length}, Substring: '{substring}'")  # Output: Length: 1, Substring: 'b'