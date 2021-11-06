import CodewarsLib.test_framework as test


# Method
def namelist(names):
    str = ""
    for name in enumerate(names, 1):
        if name[0] == len(names) - 1:
            str += f"{name[1]['name']} & "
        elif name[0] == len(names):
            str += f"{name[1]['name']}"
        else:
            str += f"{name[1]['name']}, "
    return str


# Test
def run_test():
    test.assert_equals(
        namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]),
        'Bart, Lisa, Maggie, Homer & Marge',
        "Must work with many names")
    test.assert_equals(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
                       "Must work with many names")
    test.assert_equals(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]), 'Bart & Lisa',
                       "Must work with two names")
    test.assert_equals(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
    test.assert_equals(namelist([]), '', "Must work with no names")


# Assert
run_test()
