import sys


class Solution:
    def thirdMax(self, nums) -> int:
        """ Sorting """
        nums.sort()
        
        count = 0
        i = len(nums) - 1
        while i - 1 >= 0:
            if nums[i - 1] < nums[i]:
                count = count + 1
                if count == 2:
                    return nums[i - 1]
            i = i - 1
        return nums[-1]


if __name__ == '__main__':
    # nums = [5, 4, 3, 2, 1]\
    nums = map(int, sys.argv[1:])
    nums = list(nums)
    # import pdb; pdb.set_trace()
      
    s = Solution()
    ret = s.thirdMax(nums)
    print(ret)
