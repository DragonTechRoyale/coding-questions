def isValid(s: str) -> bool:
    stack = []
    '''
    old solution:
    stack.append(s[0])
    for i in range(1, len(s)):
        c = s[i]
        prev = stack.pop()
        if prev == '(' and c != '(':
            return False
        if prev == '{' and c == '{':
            return False
        if prev == '[' and c == '[' :
            return False
        stack.append(c)
    '''        
    open = "([{"
    close = ")]}"
    all = "([{}])"
    
    if s[-1] in open or s[0] in close:
        return False
    
    for i in range(3):
        if s.count(open[i]) != s.count(close[i]):
            return False
    
    for c in s:
        if c in open:
            stack.append(c)
        elif c in close:
            recent = stack.pop()
            if (c == ')' and (recent in '[{}])')) or (c == ']' and (recent in '({}])')) or (c == '}' and (recent in '([}])')):
                return False
    return True
    
print(isValid("()[]{}"))