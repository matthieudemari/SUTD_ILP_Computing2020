def checkConsecutive(l): 
    return sorted(l) == list(range(min(l), max(l)+1)) 
print(checkConsecutive(lst))