class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        n = len(A)

        # Convert array-formatted -> decimal-formatted
        S = 0
        for i in range(n):
            S += A[i] * pow(10, n-i-1)

        # Additition Operation
        S += K

        # Convert back to array format
        i = 0
        while S != 0:
            try:
                t = S // 10
                r = S - 10*t
                A[i] = r
                S = t
                i += 1
            except IndexError:
                A.append(r)

        return A[::-1]

