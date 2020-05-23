import CodewarsLib.test_framework  as test


# Logic
def abbrevName(name):
    return f"{name.split()[0][0].upper()}.{name.split()[1][0].upper()}"


# Test
def run_test():
    test.assert_equals(abbrevName("Sam Harris"), "S.H")
    test.assert_equals(abbrevName("Patrick Feenan"), "P.F")
    test.assert_equals(abbrevName("Evan Cole"), "E.C")
    test.assert_equals(abbrevName("P Favuzzi"), "P.F")
    test.assert_equals(abbrevName("David Mendieta"), "D.M")


# Execute
run_test()
