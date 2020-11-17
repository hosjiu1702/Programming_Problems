class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Sorting
        arr.sort()

        lucky_integer = -1
        n = len(arr)
        c = 1
        for i in range(n):
            try:
                if arr[i] == arr[i+1]:
                    c += 1
                else:
                    if c == arr[i]:
                        if arr[i] > lucky_integer:
                            lucky_integer = arr[i]
                    c = 1
            except IndexError:
                if c == arr[i]:
                    if arr[i] > lucky_integer:
                        lucky_integer = arr[i]

        return lucky_integer
