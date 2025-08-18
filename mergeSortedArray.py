class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Pointers for nums1, nums2, and the merged position
        i, j, k = m - 1, n - 1, m + n - 1  

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements left
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
