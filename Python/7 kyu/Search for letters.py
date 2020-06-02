import CodewarsLib.test_framework as test
import string


# Arrange
def change(text):
    text = text.lower()
    return "".join([str(1) if letter in text else str(0) for letter in string.ascii_lowercase])


# Act
def run_test():
    test.assert_equals(change("a **&  bZ"), "11000000000000000000000001")
    test.assert_equals(change('Abc e  $$  z'), "11101000000000000000000001")
    test.assert_equals(change("!!a$%&RgTT"), "10000010000000000101000000")
    test.assert_equals(change(""), "00000000000000000000000000", "empty string should return 26 '0'")
    test.assert_equals(change("abcdefghijklmnopqrstuvwxyz"), "11111111111111111111111111")
    test.assert_equals(change("aaaaaaaaaaa"), "10000000000000000000000000")
    test.assert_equals(change("&%&%/$%$%$%$%GYtf67fg34678hgfdyd"), "00010111000000000001000010")


# Assert
run_test()
