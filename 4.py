class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        k=0
        nums=[0]*(len(nums1)+len(nums2))
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                nums[k]=nums1[i]
                i+=1
            else:
                nums[k]=nums2[j]
                j+=1
            k+=1
        while i<len(nums1):
            nums[k]=nums1[i]
            i+=1
            k+=1
        while j<len(nums2):
            nums[k]=nums2[j]
            j+=1
            k+=1
        if k%2==0:
            return (nums[k/2-1]+nums[k/2])/2.0
        else:
            return nums[(k-1)/2]