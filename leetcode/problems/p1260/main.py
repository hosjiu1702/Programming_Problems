class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nrow = len(grid)
        ncol = len(grid[0])
        steps = nrow * ncol
        for _ in range(k):
            r = 0
            c = 0
            temp = grid[0][0]
            for x in range(steps + 1):
                temp_ = grid[r][c]
                grid[r][c] = temp
                temp = temp_
                c = c + 1
                if (x + 1) % ncol == 0 and r + 1 == nrow:
                    r = 0
                    c = 0
                elif (x + 1) % ncol == 0:
                    r = r + 1
                    c = 0
                else:
                    pass

        return grid

