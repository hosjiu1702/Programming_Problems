class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        prerequisite = False
        cond1 = False
        cond2 = False
        n = len(A)
        if n < 3:
            return False

        is_peak = False
        curr_elem = A[0]
        for i in range(1, n):
            if not is_peak:
                if curr_elem < A[i]:
                    curr_elem = A[i]
                    prerequisite = True
                elif curr_elem == A[i]:
                    return False
                else:
                    curr_elem = A[i]
                    is_peak = True
                    cond1 = True
                    cond2 = True
            else:
                if curr_elem > A[i]:
                    curr_elem = A[i]
                elif curr_elem <= A[i]:
                    cond2 = False
                    break

        return cond1 and cond2 and prerequisite
