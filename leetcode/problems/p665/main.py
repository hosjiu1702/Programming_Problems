def is_last_elem(index: int, array: List[int]) -> bool:
    if index == len(array) - 1:
        return True
    return False

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        size = len(nums)
        if size <= 2:
            return True
        t = nums[0]
        i = 1
        count = 0
        is_halt = False
        while i < size and is_halt is False:
            if t <= nums[i]:
                t = nums[i]
                i += 1
                continue
            if is_last_elem(index=i, array=nums):
                count += 1
                break
            # Handle block
            while not is_last_elem(index=i, array=nums):
                if nums[i] <= nums[i+1]:
                    i += 1
                else:
                    i += 1
                    break
            if i == size - 1:
                is_halt = True
            count += 1

        if count > 1:
            return False
        return True
