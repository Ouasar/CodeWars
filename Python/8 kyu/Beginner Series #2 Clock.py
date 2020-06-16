import CodewarsLib.test_framework  as test


# Method
def past(h, m, s):
    return s * 1000 + m * 60000 + h * 3600000


# Test
def run_test():
    test.assert_equals(past(0, 1, 1), 61000)
    test.assert_equals(past(1, 1, 1), 3661000)
    test.assert_equals(past(0, 0, 0), 0)
    test.assert_equals(past(1, 0, 1), 3601000)
    test.assert_equals(past(1, 0, 0), 3600000)


# Assert
run_test()
