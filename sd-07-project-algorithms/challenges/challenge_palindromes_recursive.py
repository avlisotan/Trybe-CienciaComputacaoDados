def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if word == "":
        return False
    if len(word) < 2:
        return True
    if word[low_index] != word[high_index]:
        return False
    word = word[1:-1]
    return is_palindrome_recursive(word, low_index, len(word) - 1)
