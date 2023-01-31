def reverse_string(word):
    if str(word) == str(word)[::-1]:
        return True
    else:
        return False


def is_palindrome_iterative(word):
    if not word:
        return False

    word_invert = reverse_string(word)
    return word_invert
