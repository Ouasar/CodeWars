import CodewarsLib.test_framework as test


# Method
def add_binary(a, b):
    return bin(a + b)[2:]


# Test
def run_test():
    test.assert_equals(add_binary(1, 1), "10")
    test.assert_equals(add_binary(0, 1), "1")
    test.assert_equals(add_binary(1, 0), "1")
    test.assert_equals(add_binary(2, 2), "100")
    test.assert_equals(add_binary(51, 12), "111111")


# Assert
run_test()
