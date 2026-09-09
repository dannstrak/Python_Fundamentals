def value_counts (cadena):
    counter = {}
    for letter in cadena :
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

# Two different words and save the results in a dictionaries.
counter1 = value_counts('brontosaurus')
counter2 = value_counts('apatosaurus')

# Add_counters
def add_counters (diccionario1, diccionario2):
    newDictionarie = dict(diccionario1)
    for elementos in diccionario2 :
        if elementos not in newDictionarie:
            newDictionarie[elementos] = diccionario2[elementos]
        else:
            newDictionarie[elementos] += diccionario2[elementos]
    return newDictionarie