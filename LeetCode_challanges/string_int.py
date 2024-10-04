def myAtoi(s:str) -> int:

    INT_MIN, INT_MAX = -2**31, 2*31 - 1

    s = s.lstrip()

    sign = 1
    index = 0
    if s[index] < len(s):
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1


    # Step3: Read digits and skip leading zeros
    num = 0
    while index < len(s) and s[index].isdigit():
        digit = int(s[index])
        #Step 4 : Handle overflow

        if num > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        num = num * 10 + digit
        index += 1

        #step 5: Apply sign
        return sign * num