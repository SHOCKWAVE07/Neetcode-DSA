class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for i in strs:
            encoded+= str(len(i))
            encoded+="#"
            encoded+=i

        return encoded



    def decode(self, s: str) -> List[str]:
        ans = []
        cnt = ""
        i = 0
        while i <= len(s)-1:
            if s[i] == "#":
                digit = int(cnt)
                if digit:
                    ans.append(s[i+1:i+1+digit])
                else:
                    ans.append("")
                i+=digit
                cnt = ""
            else:
                cnt+=s[i]
            i+=1
            
   
        return ans


