# Problem Link: https://takeuforward.org/data-structure/find-second-smallest-and-second-largest-element-in-an-array/

class Solution:
    def findSecondSmallest(self, nums):
        first = second = float('inf')
        for num in nums:
            if num < first:
                second = first
                first = num
            elif first < num < second:
                second = num
        return second if second != float('inf') else -1
    
    def findSecondLargest(self, nums):
        first = second = float('-inf')
        for num in nums:
            if num > first:
                second = first
                first = num
            elif second < num < first:
                second = num
        return second if second != float('-inf') else -1

    def findSecondSmallestAndLargest(self, nums):
        return self.findSecondSmallest(nums), self.findSecondLargest(nums)

# Time Complexity: O(n)
# Space Complexity: O(1)

solution = Solution()
input = [1, 2, 3, 4, 5]
res = solution.findSecondSmallestAndLargest(input)
print(res)  # Output: (2, 4)