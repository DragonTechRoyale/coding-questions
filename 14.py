def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""
    smallest_str = min(strs, key=len)
    
    for i in range(len(smallest_str)):
        still_prefix = True
        c = smallest_str[i]
        
        for current_str in strs:
            if current_str[i] != c:
                still_prefix = False
                break
            
        if still_prefix:
            prefix += c
        else:
            break                
        
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))