def find_repets(counter):
    newList = []
    for elements in counter:
        if counter[elements] > 1:
            newList.append(elements)
    return newList


