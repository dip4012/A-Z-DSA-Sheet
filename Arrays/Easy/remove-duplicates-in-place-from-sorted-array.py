# Problem Link: https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1

# Time Complexity: O(n)
# Space Complexity: O(1)

solution = Solution()
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
k = solution.removeDuplicates(arr)
print(arr[:k])