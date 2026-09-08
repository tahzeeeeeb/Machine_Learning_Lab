def removeDuplicate(values):
    nonDuplicateList = []
    for item in values:
        if item not in nonDuplicateList:
            nonDuplicateList.append(item)
    return nonDuplicateList

values = [1, 2, 2, 2, 3, 4, 1, 4, 5]
print(removeDuplicate(values))
