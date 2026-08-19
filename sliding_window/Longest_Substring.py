# Given a string s, find the length of the longest substring without repeating characters.

# s = "abcabcbb"
# Longest substring:
# "abc"
# Length : 3
# Output = 3

def lengthOfLongestSubstring(s):
    chars = set()          # Stores unique characters in current window
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If duplicate character exists, shrink the window
        while s[right] in chars:
            chars.remove(s[left])
            left += 1

        # Add current character
        chars.add(s[right])

        # Update maximum length
        max_length = max(max_length, right - left + 1)

    return max_length


s = "abcabcbb"
print(lengthOfLongestSubstring(s))