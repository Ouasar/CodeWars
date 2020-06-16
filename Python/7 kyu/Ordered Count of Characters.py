import CodewarsLib.test_framework as test
from collections import Counter


# Method
def ordered_count(inp):
    return list(Counter(inp).items())


# Test
def run_test():
    tests = (
        ('ab', [('a', 1), ('b', 1)]),
        ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
        ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
    )

    for t in tests:
        inp, exp = t
        test.assert_equals(ordered_count(inp), exp)


# Assert
run_test()
