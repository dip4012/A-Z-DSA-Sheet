# Problem Link: https://takeuforward.org/data-structure/left-rotate-the-array-by-one/

class Solution:
    def leftRotateByOne(self, arr):
        if not arr:
            return

        firstEle = arr[0]

        for i in range(len(arr) - 1):
            arr[i] = arr[i + 1]
        
        arr[-1] = firstEle

# Time Complexity: O(n)
# Space Complexity: O(1)

solution = Solution()
arr = [1, 2, 3, 4, 5]
solution.leftRotateByOne(arr)
print(arr)