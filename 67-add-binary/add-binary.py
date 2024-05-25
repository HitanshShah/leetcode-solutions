class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la, lb = len(a)-1, len(b)-1
        carry = 0
        ans = ""
        while la >= 0 or lb >= 0 or carry == 1:
            val = 0
            if(la >= 0):
                val += int(a[la])
                la -= 1
            if(lb >= 0):
                val += int(b[lb])
                lb -= 1
            val += carry
            carry = val//2
            val = val%2
            print(str(val))
            ans = ans + str(val)
        return "".join(reversed(ans))