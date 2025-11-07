# Problem Link: https://takeuforward.org/data-structure/find-the-largest-element-in-an-array/

class Solution:
    def largestElement(self, nums):
        max_ele = -10000
        for num in nums:
            if num > max_ele:
                max_ele = num
        return max_ele

# Time Complexity: O(n)
# Space Complexity: O(1)

solution = Solution()
input = [1, 2, -3]
res = solution.largestElement(input)
print(res)