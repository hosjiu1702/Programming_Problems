from typing import List


class Carrier(list):
    def __init__(self):
        super(Carrier, self)

    def insert_missing_numbers(self, i, j, arr):
        s = arr[j] - i
        for _ in range(s):
            self.append(i)
            i = i + 1


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l_arr = len(arr)
        m = Carrier()
        i = 1
        j = 0
        while j <= l_arr - 1:
            m.insert_missing_numbers(i, j, arr)
            i = arr[j] + 1
            j = j + 1

        t = len(m)

        if k <= t:
            return m[k-1]

        return arr[-1] + k - t

