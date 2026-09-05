class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastsum = {}
        for i in range(len(nums)) : 
            if target-nums[i] in pastsum:
                return [pastsum[target-nums[i]],i]
            pastsum[nums[i]] = i

        