import CodewarsLib.test_framework  as test

# Arrange
languages_database = {
    'english': 'Welcome',
    'czech': 'Vitejte',
    'danish': 'Velkomst',
    'dutch': 'Welkom',
    'estonian': 'Tere tulemast',
    'finnish': 'Tervetuloa',
    'flemish': 'Welgekomen',
    'french': 'Bienvenue',
    'german': 'Willkommen',
    'irish': 'Failte',
    'italian': 'Benvenuto',
    'latvian': 'Gaidits',
    'lithuanian': 'Laukiamas',
    'polish': 'Witamy',
    'spanish': 'Bienvenido',
    'swedish': 'Valkommen',
    'welsh': 'Croeso'}


def greet(word):
    if languages_database.get(word) is None:
        return "Welcome"
    else:
        return languages_database.get(word)


# Act
def run_test():
    test.describe("Basic tests")
    test.assert_equals(greet('english'), 'Welcome')
    test.assert_equals(greet('dutch'), 'Welkom')
    test.assert_equals(greet('IP_ADDRESS_INVALID'), 'Welcome')
    test.assert_equals(greet(''), 'Welcome')
    test.assert_equals(greet(2), 'Welcome')


# Assert
run_test()
