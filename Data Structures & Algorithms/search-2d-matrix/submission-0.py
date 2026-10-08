class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break   

        # If the row doesn't exist the pointers will cross.
        if not (top <= bottom):
            return False

        # Once we get the correct row.
        # We need to know if the value is in the row or not.

        L = 0
        R = len(matrix[mid]) - 1

        while L <= R:
            col = (L+R) // 2

            if matrix[mid][col] == target:
                return True
            elif matrix[mid][col] < target:
                L= col +1
            elif matrix[mid][col] > target:
                R = col - 1
            
        return False