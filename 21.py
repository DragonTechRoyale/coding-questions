
def mergeTwoLists(list1: list, list2: list) -> list:
    merged = []
    current1 = 0
    current2 = 0
    
    min_list = min([list1, list2], key=len)
    for item in min_list:
        current1 = list1[0]
        current2 = list2[0]
        
        del list1[0]
        del list2[0]
        
        merged.append(min(current1, current2))
        merged.append(max(current1, current2))
        
    merged += list1
    merged += list2
    
    return merged

print(mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))