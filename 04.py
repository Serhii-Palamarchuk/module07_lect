from collections import Counter

def is_anagram(word1, word2):
    """
    Checks whether the words are anagrams.

    word1: string
    word2: string

    returns: boolean
    """
    # Convert both words to lowercase to ensure the comparison is case-insensitive
    word1 = word1.lower()
    word2 = word2.lower()

    # Check if the sorted characters of both words are the same
    return sorted(word1) == sorted(word2)

# Example usage
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False


def is_anagram2(word1, word2):
    """
    Checks whether the words are anagrams.

    word1: string
    word2: string

    returns: boolean
    """
    # Convert both words to lowercase to ensure the comparison is case-insensitive
    word1 = word1.lower()
    word2 = word2.lower()

    # Check if the sorted characters of both words are the same
    return Counter(word1) == Counter(word2)

# Example usage
print(is_anagram2("listen", "silent"))  # Output: True
print(is_anagram2("hello", "world"))    # Output: False


