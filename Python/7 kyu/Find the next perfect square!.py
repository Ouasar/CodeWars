import CodewarsLib.test_framework  as test
import math


# Arrange
def find_next_square(number: int):
    sqrt = math.sqrt(number)

    if sqrt == int(sqrt):
        return int((sqrt + 1) ** 2)
    return -1


# Act
def run_test():
    test.describe("find_next_square")

    test.it("should return the next square for perfect squares")
    test.assert_equals(find_next_square(121), 144, "Wrong output for 121")
    test.assert_equals(find_next_square(625), 676, "Wrong output for 625")
    test.assert_equals(find_next_square(319225), 320356, "Wrong output for 319225")
    test.assert_equals(find_next_square(15241383936), 15241630849, "Wrong output for 15241383936")

    test.it("should return -1 for numbers which aren't perfect squares")
    test.assert_equals(find_next_square(155), -1, "Wrong output for 155")
    test.assert_equals(find_next_square(342786627), -1, "Wrong output for 342786627")


# Assert
run_test()
