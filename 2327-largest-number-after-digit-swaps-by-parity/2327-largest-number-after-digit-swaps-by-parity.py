class Solution:
    def largestInteger(self, num: int) -> int:
        nums = [int(i) for i in str(num)]

        def jud(num):
            return True if num%2 == 0 else False
        

        for i in range(len(nums)):
            flag = jud(nums[i])
            maxValue = nums[i]
            for j in range(i+1,len(nums)):
                if flag == jud(nums[j]):
                    if maxValue < nums[j]:
                        maxValue = nums[j]
                        nums[i],nums[j] = nums[j],nums[i]

        return int("".join(map(str, nums)))
                