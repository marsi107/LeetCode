
# There is a robot on an m x n grid. 
# m is height
# n is width
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = 0
        grid = [[height_item+1 for height_item in range(m)] for width_item in range(n)]
        #grid = ["width_item" for width_item in range(n)]
        for height_item in range(1, m):
            for width_item in range(1, n):
                grid[height_item][width_item] = grid[height_item-1][width_item] + grid[height_item][width_item-1]
        return grid

sol_class = Solution()
print(sol_class.uniquePaths(3, 2))