class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for i in range(len(nums)):
            mp[nums[i]]= i
        
        for i in range(len(nums)):
            k = target - nums[i]
            if k in mp:
                x = mp[k]
                if i!=x:
                    return [i,x] if i<x else [x,i]

        