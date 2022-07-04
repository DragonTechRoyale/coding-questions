# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
from random import randrange

def guess(num: int) -> int

class Solution:
    def guessNumber(self, n: int) -> int:
        #num = randrange(n+1)
        
        end = n 
        start = 0
        middle = (start + end) // 2
        
        while True:
            if guess(middle) == -1:
                start = middle + 1
                middle = (start + end) // 2
            elif guess(middle) == 1:
                end = middle
                middle = (start + end) // 2
            elif guess(middle) == 0:
                return middle
            if start >= end:
                break
        return middle