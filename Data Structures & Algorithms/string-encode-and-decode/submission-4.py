class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            x = len(s)
            r = r + str(x) + "!"+s

        return r;
        

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: 
            return []

        r = []
        while (len(s) > 0):

            # getting the length of digit
            sep = s.find("!")
            n = int(s[:sep])
            r.append(s[sep+1:sep+1+n])
            s = s[sep+1+n:]
            
        return r




