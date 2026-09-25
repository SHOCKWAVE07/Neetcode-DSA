class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = dict()

        for i in strs:

            arr = [0]*26

            for j in i:
                arr[ord(j) - ord('a')] += 1

            key = tuple(arr)

            if key not in mp:
                mp[key] = [i]
            else:
                mp[key].append(i)
        
        output = []
        for i,k in mp.items():
          
            output.append(k)
        return output






        