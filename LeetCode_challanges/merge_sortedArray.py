class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Initialize three pointers
        p1 = m - 1  # Last element of the valid part of nums1
        p2 = n - 1  # Last element of nums2
        p = m + n - 1  # Last position of nums1

        # While both pointers p1 and p2 are valid
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are any remaining elements in nums2, copy them
        # This step is necessary only if p2 is still >= 0.
        # If p1 finishes first, nums1 is already sorted.
        nums1[:p2 + 1] = nums2[:p2 + 1]