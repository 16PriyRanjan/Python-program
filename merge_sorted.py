def merge(nums1, m, nums2, n):
   """
   Merges two sorted arrays `nums1` and `nums2` into `nums1` in-place.

   Args:
       nums1: The first sorted array, with extra space at the end to accommodate the merged elements.
       m: The number of elements in `nums1` to consider for merging.
       nums2: The second sorted array.
       n: The number of elements in `nums2`.

   Returns:
       None. The merged result is stored in `nums1` in-place.
   """

   p1 = m - 1  # Pointer for the last element in the valid part of nums1
   p2 = n - 1  # Pointer for the last element in nums2
   p = m + n - 1  # Pointer for the last element in the merged array

   while p1 >= 0 and p2 >= 0:
       if nums1[p1] >= nums2[p2]:
           nums1[p] = nums1[p1]
           p1 -= 1
       else:
           nums1[p] = nums2[p2]
           p2 -= 1
       p -= 1

   # Copy remaining elements from nums2 (if any) to nums1
   nums1[:p2 + 1] = nums2[:p2 + 1]
