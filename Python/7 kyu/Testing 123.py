import CodewarsLib.test_framework as test


# Method
def number(lines):
    return [f"{i}: {j}" for i, j in enumerate(lines, 1)]


# Test
def run_test():
    test.assert_equals(number([]), [])
    test.assert_equals(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])


# Assert
run_test()
