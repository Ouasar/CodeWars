import CodewarsLib.test_framework as Test
import re


# Method
def validate_pin(pin):
    return re.search(r'[\D]', pin) is None and (len(pin) == 4 or len(pin) == 6)


# Test
def run_test():
    Test.assert_equals(validate_pin("12"), False, "Wrong output for '12'")
    Test.assert_equals(validate_pin("123"), False, "Wrong output for '123'")
    Test.assert_equals(validate_pin("12345"), False, "Wrong output for '12345'")
    Test.assert_equals(validate_pin("1234567"), False, "Wrong output for '1234567'")
    Test.assert_equals(validate_pin("-1234"), False, "Wrong output for '-1234'")
    Test.assert_equals(validate_pin("1.234"), False, "Wrong output for '1.234'")
    Test.assert_equals(validate_pin("00000000"), False, "Wrong output for '00000000'")
    Test.assert_equals(validate_pin("12.0"), False)
    Test.assert_equals(validate_pin("123456x"), False)

    Test.assert_equals(validate_pin("a234"), False, "Wrong output for 'a234'")
    Test.assert_equals(validate_pin(".234"), False, "Wrong output for '.234'")
    Test.assert_equals(validate_pin("-123"), False, "Wrong output for '-123'")
    Test.assert_equals(validate_pin("-1.234"), False, "Wrong output for '-1.234'")

    Test.assert_equals(validate_pin("1234"), True, "Wrong output for '1234'")
    Test.assert_equals(validate_pin("0000"), True, "Wrong output for '0000'")
    Test.assert_equals(validate_pin("1111"), True, "Wrong output for '1111'")
    Test.assert_equals(validate_pin("123456"), True, "Wrong output for '123456'")
    Test.assert_equals(validate_pin("098765"), True, "Wrong output for '098765'")
    Test.assert_equals(validate_pin("000000"), True, "Wrong output for '000000'")
    Test.assert_equals(validate_pin("123456"), True, "Wrong output for '123456'")
    Test.assert_equals(validate_pin("090909"), True, "Wrong output for '090909'")


# Assert
run_test()

