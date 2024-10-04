'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

'''
def isMatch(s: str, p: str) -> bool:
    # Create a DP table with dimensions (len(s) + 1) x (len(p) + 1)
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Empty string and empty pattern are a match
    dp[0][0] = True
    
    # Handle patterns that can match empty string, e.g., "a*", "a*b*"
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    # Fill the table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # Current character in pattern matches the current character in string
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' means zero or more of the previous element
                dp[i][j] = dp[i][j - 2]  # Case when '*' matches zero preceding element
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # Case when '*' matches one or more preceding elements
    
    # The answer is whether the entire string matches the entire pattern
    return dp[len(s)][len(p)]

# Example usage:
s = "aa"
p = "a"
print(isMatch(s, p))  # Output: False
