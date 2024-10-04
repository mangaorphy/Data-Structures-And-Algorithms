class Solution(object):
    def search(self, nums, target, callback=None):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        :param callback: A function to call with the current mid value.
        """
        start = 0
        end = len(nums) - 1

        while start <= end:  # Continue until the search space is empty
            mid = (start + end) // 2  # Find the middle index
            
            # Call the callback function with the current mid value, if provided
            if callback:
                callback(nums[mid])

            if target == nums[mid]:
                return mid  # Target found
            elif target < nums[mid]:
                end = mid - 1  # Move the end pointer left
            else:
                start = mid + 1  # Move the start pointer right

        return -1  # Target not found

# Example usage
def my_callback(value):
    print(f"Checking value: {value}")

solution = Solution()
result = solution.search([1, 2, 3, 4, 5], 3, callback=my_callback)
print("Result index:", result)