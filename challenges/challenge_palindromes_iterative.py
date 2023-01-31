def is_palindrome(word):
    if str(word) == str(word)[::-1]:
        return True
    else:
        return False


def is_palindrome_iterative(word):
    if not word:
        return False

    return is_palindrome(word)
