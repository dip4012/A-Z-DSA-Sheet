# Problem Link: https://takeuforward.org/data-structure/check-if-an-array-is-sorted/

class Solution:
    def isSorted(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True

# Time Complexity: O(n)
# Space Complexity: O(1)

solution = Solution()
nums = [1,2,2,3,5,4]
res = solution.isSorted(nums)
print(res)