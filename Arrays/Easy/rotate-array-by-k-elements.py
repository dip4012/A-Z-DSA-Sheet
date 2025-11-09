# Problem Link: https://takeuforward.org/data-structure/rotate-array-by-k-elements/

class Solution:
    def reverse(self, arr, start, end):
        while(start <= end):
            (arr[start], arr[end]) = (arr[end], arr[start])
            start += 1
            end -= 1

    def rotateToRight(self, arr, n, k):
        self.reverse(arr, 0, n - k - 1)
        self.reverse(arr, n - k, n - 1)
        self.reverse(arr, 0, n - 1)
    
    def rotateToLeft(self, arr, n, k):
        self.reverse(arr, 0, k - 1)
        self.reverse(arr, k, n - 1)
        self.reverse(arr, 0, n - 1)

# Time Complexity: O(n)
# Space Complexity: O(1)

solution = Solution()
arr = [1, 2, 3, 4, 5]
# solution.rotateToLeft(arr, 5, 3)
solution.rotateToRight(arr, 5, 3)
print(arr)