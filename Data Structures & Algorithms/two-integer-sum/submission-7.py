class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_mapping = {}
        for have_idx,have in enumerate(nums):
            want = target - have
            if want in index_mapping:
                return [index_mapping[want],have_idx]
            else:
                index_mapping[have]=have_idx
            