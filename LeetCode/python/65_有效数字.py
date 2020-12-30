class Solution:
    def isNumber(self, s: str) -> bool:

        s = s.strip()
        point_seen = False
        num_seen = False
        e_seen = False
        num_after_e = False

        for i in range(len(s)):
            if s[i] >= "0" and s[i] <= "9":
                num_seen = True
                num_after_e = True
            elif s[i] == ".":
                if e_seen or point_seen:
                    return False
                point_seen = True
            elif s[i] == "e":
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_after_e = False
            elif s[i] == "-" or s[i] == "+":
                if i > 0 and s[i - 1] != "e":
                    return False
            else:
                return False
        return num_seen and num_after_e