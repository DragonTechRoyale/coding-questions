def romanToInt(s: str) -> int:
    roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    pairs = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    
    sum = 0
    i = 0
    num = 0
    final_pair = False # checks if the current pair (ex: 'IV'), is the last in the string. If it is, don't add the last character after the while loop.
    is_current_pair = False # checks if the current iteration is a pair. If it is not, add to the sum the current number


    while i < len(s)-1:
        c = s[i] # c - current
        n = s[i+1] # n - next
        is_current_pair = c+n in pairs
        
        if is_current_pair:
            i += 1 # Skip the next number
            final_pair = i == len(s)-1

            if c == 'I':
                if n == 'V':
                    num = 4
                elif n == 'X':
                    num = 9
            elif c == 'X':
                if n == 'L':
                    num = 40
                elif n == 'C':
                    num = 90
            elif c == 'C':
                if n == 'D':
                    num = 400
                elif n == 'M':
                    num = 900
                    
        if not is_current_pair:
            num = roman[c]
            
        sum += num
        i += 1
    
    if not final_pair:
        sum += roman[s[-1]]
    
    return sum

print(romanToInt("DCXXI"))

'''
final solution in leetcode (slightly faster):

class Solution:
    roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    pairs = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        num = 0
        final_pair = False # checks if the current pair (ex: 'IV'), is the last in the string. If it is, don't add the last character after the while loop.
        is_current_pair = False # checks if the current iteration is a pair. If it is not, add to the sum the current number


        while i < len(s)-1:
            c = s[i] # c - current
            n = s[i+1] # n - next
            is_current_pair = c+n in self.pairs

            if is_current_pair:
                i += 1 # Skip the next number
                final_pair = i == len(s)-1

                if c == 'I':
                    if n == 'V':
                        num = 4
                    elif n == 'X':
                        num = 9
                elif c == 'X':
                    if n == 'L':
                        num = 40
                    elif n == 'C':
                        num = 90
                elif c == 'C':
                    if n == 'D':
                        num = 400
                    elif n == 'M':
                        num = 900

            if not is_current_pair:
                num = self.roman[c]

            sum += num
            i += 1

        if not final_pair:
            sum += self.roman[s[-1]]

        return sum
'''