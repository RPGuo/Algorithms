### 双指针 o(M+N)的解法
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        count = (m+n)//2 + 1
        l1, l2 = 0, 0
        left, right = 0, 0
        for i in range(count):
            left = right
            if l1<m and (l2>=n or (nums1[l1]<nums2[l2])):
                right = nums1[l1]
                l1 += 1
            else:
                right = nums2[l2]
                l2 += 1
        if (m+n)&1 == 1:
            return right
        else:
            return (left + right)/2.0

### log(m+n)解法
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        target1 = (m+n+1)//2
        target2 = (m+n+2)//2
        return (self.getK(nums1, 0, m-1, nums2, 0, n-1, target1) + self.getK(nums1, 0, m-1, nums2, 0, n-1, target2))/2.0
    def getK(self, nums1, l1, r1, nums2, l2, r2, k):
        len1 = r1 - l1 + 1
        len2 = r2 - l2 + 1
        if len1 > len2:
            return self.getK(nums2, l2, r2, nums1, l1, r1, k)
        if len1 == 0:
            return nums2[l2 + k - 1]
        if k == 1:
            return min(nums1[l1], nums2[l2])
        mid1 = l1 + min(len1, k//2) - 1
        mid2 = l2 + min(len2, k//2) - 1
        if nums1[mid1] > nums2[mid2]:
            return self.getK(nums1, l1, r1, nums2, mid2+1, r2, k-min(len2, k//2))
        else:
            return self.getK(nums1, mid1+1, r1, nums2, l2, r2, k-min(len1, k//2))
### O(log(min(m,n)))
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        i_min, i_max = 0, len(nums1)
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = (m + n + 1) // 2 - i
            if i != m and j != 0 and nums2[j - 1] > nums1[i]:
                i_min = i + 1
            elif i != 0 and j != n and nums1[i - 1] > nums2[j]:
                i_max = i - 1
            else:
                max_left = 0
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) & 1 == 1:
                    return max_left

                min_right = 0
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                return (max_left + min_right) / 2.0
        return 0