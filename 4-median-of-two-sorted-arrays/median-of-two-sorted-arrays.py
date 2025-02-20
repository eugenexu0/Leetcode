class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        length = len(nums1) + len(nums2)
        index = length // 2 + 1
        #make the merged array
        i = j = 0


        while (i < len(nums1) and j < len(nums2)):
            if (nums1[i] < nums2[j]):
                merged.append(nums1[i])
                i = i + 1
            else:
                merged.append(nums2[j])
                j = j + 1
        while (i < len(nums1)):
            merged.append(nums1[i])
            i += 1
        while (j < len(nums2)):
            merged.append(nums2[j])
            j += 1
        k = length // 2
        if (length % 2 == 0):
            return (merged[k] + merged[k-1]) / 2.0
        else:
            return (merged[k])


        