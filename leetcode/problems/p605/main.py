from math import floor

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        zeros = 0
        c = 0
        if flowerbed[0] == 0:
            j = 0
            zeros = 0
            while j < l:
                if flowerbed[j] != 1:
                    zeros += 1
                    j += 1
                    continue
                break
            c += floor(zeros) // 2
            zeros = 0
        for i in range(l):
            if flowerbed[i] == 1:
                if zeros > 0:
                    c += floor(zeros - 1) // 2
                    zeros = 0
                continue
            zeros += 1
        if zeros:
            c += floor(zeros // 2)
        if n <= c:
            return True
        return False
