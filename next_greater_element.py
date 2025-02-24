# For each element in nums1, find the index j such that nums1[i] == nums2[j] and 
# determine the next greater element of nums2[j] in nums2. 
# If there is no next greater element, then the answer for this query is -1.
class Solution(object):
    def nextGreaterElementBruteForce(self, nums1, nums2):
        """
        Brute force solution using hashmap
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arr = []
        ind = {}
        for i,v in enumerate(nums2):
            ind[v] = i
        for i,v in enumerate(nums1):
            idx = ind[v]
            if idx < len(nums2)-1:
                for j in range(idx+1,len(nums2)):
                    if nums2[j] > v:
                        arr.append(nums2[j])
                        break
                    elif j==len(nums2)-1:
                        arr.append(-1)
            else:
                arr.append(-1)
        return arr

    def nextGreaterElementUsingStack(self, nums1, nums2):
            """
            Solution using monotonic stack and hashmap
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
            stk = []
            ind = {}
            n = len(nums1)
            res = [-1]*n
            for i,v1 in enumerate(nums1):
                ind[v1] = i
            for j,v2 in enumerate(nums2):
                while stk and v2 > stk[-1]:
                    val = stk.pop()
                    if val in nums1:
                        res[ind[val]] = v2
                stk.append(v2)
            return res
      
def main():
    obj = Solution()
    print(obj.nextGreaterElementBruteForce([2,4],[1,2,3,4]))
    print(obj.nextGreaterElementUsingStack([2,4],[1,2,3,4]))
  
if __name__ == '__main__':
    main()
