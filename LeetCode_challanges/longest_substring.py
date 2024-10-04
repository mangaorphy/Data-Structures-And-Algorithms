
'''
Given a string s, find the length of the longest substring without repeating characters
'''

def longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If we found a duplicate character, move the current pointer

        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1

        char_set.add(right)
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
s = "abcabcbb"
print(longest_substring(s))  # Output: 3