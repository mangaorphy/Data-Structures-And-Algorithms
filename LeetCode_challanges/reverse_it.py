def reverse_integer(x: int) -> int:
    # Define the 32-bit signed integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # Determine the sign of x
    sign = -1 if x < 0 else 1
    x *= sign  # Make x positive for easier manipulation
    
    # Reverse the digits of x
    reversed_x = int(str(x)[::-1])
    
    # Restore the sign
    reversed_x *= sign
    
    # Check for overflow and return the result
    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0
    return reversed_x

# Example usage
print(reverse_integer(123))    # Output: 321
print(reverse_integer(-123))   # Output: -321
print(reverse_integer(120))    # Output: 21
print(reverse_integer(1534236469))  # Output: 0 (overflow case)