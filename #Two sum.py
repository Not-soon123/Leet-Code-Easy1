class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
#the optimized solution 
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            dict1={}
            for index, value in enumerate(nums):
                val= target - value
                if val in dict1:
                    return [dict1[val], index]
                else:
                    dict1[value]=index
            return []
