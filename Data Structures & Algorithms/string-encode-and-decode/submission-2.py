class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + "#" + s
            # if not enc:
            #     enc += s
            # else:
            #     enc += "#" + s
        return enc


    def decode(self, s: str) -> List[str]:
        res = []
        prev_num = 0
        x = ""
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                x += s[i]
                prev_num = 1
                i += 1
            if prev_num and s[i] == "#":
                prev_num = 0
                l = int(x)
                x = ""
                res.append(s[i+1:i+l+1])
                i = i+l+1

        return res

