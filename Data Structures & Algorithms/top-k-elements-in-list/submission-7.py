
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = dict()

        buckets = [[] for i in range(len(nums) + 1)]
        ans = []

        for i in nums:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1

        for q, v in mp.items():
            buckets[v].append(q)

        for bucket in buckets[::-1]:
            if bucket:
                ans.extend(bucket)

                if len(ans) >= k:
                    return ans[:k]

        return ans
