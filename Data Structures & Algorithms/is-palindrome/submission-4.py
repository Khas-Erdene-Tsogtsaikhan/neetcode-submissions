class Solution:
    def isPalindrome(self, s: str) -> bool:

        #start with two pointers beginning and end
        #keep comparing until we converge at the middle or if the left pointer
        #passes the right pointer. Get rid of all whitespaces as well


        #racecar

        left = 0
        right = len(s)-1

        while right>left:
            if s[left] == " " or not s[left].isalnum():
                left += 1
                continue
            if s[right] == " " or not s[right].isalnum():
                right -=1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -=1
            else:
                return False
        return True
            