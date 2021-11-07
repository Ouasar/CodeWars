import CodewarsLib.test_framework as test


# Method
def duplicate_count(text):
    countIteration = 0

    for letter in set(text.lower()):
        countIterationLetter = text.lower().count(letter)

        if countIterationLetter > 1:
            countIteration += 1

    return countIteration


# Test
def run_test():
    test.assert_equals(duplicate_count(""), 0)
    test.assert_equals(duplicate_count("abcde"), 0)
    test.assert_equals(duplicate_count("abcdeaa"), 1)
    test.assert_equals(duplicate_count("abcdeaB"), 2)
    test.assert_equals(duplicate_count("Indivisibilities"), 2)


# Assert
run_test()
