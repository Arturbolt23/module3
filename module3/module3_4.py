def single_root_words(root_words, *other_words):
    same_words = []
    root_words_lower = root_words.lower()
    for words in other_words:
        words_lower = words.lower()
        if root_words_lower in words_lower or words_lower in root_words_lower:
            same_words.append(words)
            continue
    return same_words
result = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result)
print(result_2)