from typing import List


def insertion_sort(a: List[int]) -> List[int]:
    # This algorithm is Insertion_sort (descending)
    n = len(a)
    for i in range(n):
        for j in range(i):
            if a[j] > a[i]:
                t = a[i]
                a[i] = a[j]
                a[j] = t
    return a[::-1]
    

class Solution:
        def lastStoneWeight(self, stones: List[int]) -> int:
            # Sort all stones in orders of magnitude
            stones = insertion_sort(stones)
            
            while len(stones):
                if len(stones) > 1:
                    # Get stones from the storage
                    stone1 = stones.pop(0)
                    stone2 = stones.pop(0)

                    # Smash two consecutive stones
                    new_stone = max(stone1, stone2) - min(stone1, stone2)
                    
                    if new_stone > 0:
                        n = len(stones)
                        if n == 0:
                            stones.append(new_stone)
                            continue

                        for i in range(n):
                            if new_stone >= stones[i]:
                                stones.insert(i, new_stone)
                                break
                            else:
                                if i == n - 1:
                                    stones.append(new_stone)
                else:
                    break

            return 0 if len(stones) == 0 else stones[0]

