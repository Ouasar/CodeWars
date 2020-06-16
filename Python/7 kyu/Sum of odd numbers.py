import CodewarsLib.test_framework as test


# Method
def row_sum_odd_numbers(n):
    return n * n * n;


# Test
def run_test():
    test.assert_equals(row_sum_odd_numbers(1), 1)
    test.assert_equals(row_sum_odd_numbers(2), 8)
    test.assert_equals(row_sum_odd_numbers(13), 2197)
    test.assert_equals(row_sum_odd_numbers(19), 6859)
    test.assert_equals(row_sum_odd_numbers(41), 68921)


# Assert
run_test()
