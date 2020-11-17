from collections import Counter

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        c = 0
        lenA = len(A)
        lenB = len(B)

        if lenA != lenB:
            return False

        s = []
        for i in range(lenA):
            if c > 2:
                return False
            if A[i] != B[i]:
                c += 1
                s.append(i) # append index
        try:
            if A[s[1]] == B[s[0]] and A[s[0]] == B[s[1]]:
                return True
        except IndexError:
            counter = Counter(A)
            for v in counter.values():
                if v > 1 and c == 0:
                    return True

        return False

