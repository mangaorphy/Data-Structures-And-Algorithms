'''
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
'''

'''
ALGORITHM STEPS:

1. Initialize variable max_reachable = 0 which represents the furthest index you reach
2. Loop through the array. for each index i, check if i is greater than max_reachable. If it is, return false because you cannot move beyond that point.
3. Update max_reachable to be maximum of max_reacheble and i + num[i]
4. If at any point max_reachable is greater than or equal to the lasst index, return true
'''

def canJump(nums):
    max_reachable = 0
    for i in range(len(nums)):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + nums[i])

    return True