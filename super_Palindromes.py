'''PROBLEM : Super Palindrome '''

#CODE :

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left,right = int(left),int(right)
        limit = 100000
        cnt = 0
        for i in range(1,limit):
            s = str(i)
            p = s+s[::-1][1:]
            p2 = int(p) ** 2
            if p2 > right:
                break
            if p2 >=left and str(p2) == str(p2)[::-1]:
                cnt += 1
        for i in range(limit):
            s = str(i)
            p = s + s[::-1]
            p2 = int(p) ** 2
            if p2 > right:
                break
            if p2 >= left and str(p2) == str(p2)[::-1]:
                cnt += 1
        return cnt
