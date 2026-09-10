def is_Interlocking (word, palabrasValidas):
    wordDivided = word[0::2]
    wordDivided2 = word[1::2]
    if wordDivided not in palabrasValidas and wordDivided2 not in palabrasValidas:
        return False
    else:
        return True
