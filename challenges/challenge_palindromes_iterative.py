def is_palindrome_iterative(word):
    inverso = ""

    if not word:
        return False

    for item in range(len(word) - 1, -1, -1):
        inverso += word[item]

    if inverso == word:
        return True
    else:
        return False
