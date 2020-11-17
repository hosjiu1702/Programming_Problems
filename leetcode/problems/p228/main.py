class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        ret = []
        base_index = 0
        for i in range(n):
            try:
                if nums[i+1] != nums[i] + 1:
                    if base_index == i:
                        ret.append(f"{nums[i]}")
                    else:
                        ret.append(f"{nums[base_index]}->{nums[i]}")
                    base_index = i + 1
            except IndexError:
                if base_index == i:
                    ret.append(f"{nums[i]}")
                else:
                    ret.append(f"{nums[base_index]}->{nums[i]}")
        return ret
