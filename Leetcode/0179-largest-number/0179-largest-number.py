class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def custom_sort(x, y):
            if x + y > y + x:
                return -1 
            elif x + y < y + x:
                return 1   
            else:
                return 0 
        nums = list(map(str, nums))
        sorted_nums = sorted(nums, key=cmp_to_key(custom_sort))
        if sorted_nums[0] == '0': 
            return "0"
        return "".join(sorted_nums)
