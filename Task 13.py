def get_words_starting_with_vowel(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [word for word in words if word[0].lower() in vowels]
