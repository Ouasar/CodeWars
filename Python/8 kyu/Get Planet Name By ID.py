import CodewarsLib.test_framework  as Test

# Arrange
n = {1: "Mercury",
     2: "Venus",
     3: "Earth",
     4: "Mars",
     5: "Jupiter",
     6: "Saturn",
     7: "Uranus",
     8: "Neptune"}


# Method
def get_planet_name(id):
    return {1: "Mercury",
            2: "Venus",
            3: "Earth",
            4: "Mars",
            5: "Jupiter",
            6: "Saturn",
            7: "Uranus",
            8: "Neptune"}.get(id)


# Test
def run_test():
    Test.assert_equals(get_planet_name(2), 'Venus')
    Test.assert_equals(get_planet_name(5), 'Jupiter')
    Test.assert_equals(get_planet_name(3), 'Earth')
    Test.assert_equals(get_planet_name(4), 'Mars')
    Test.assert_equals(get_planet_name(8), 'Neptune')
    Test.assert_equals(get_planet_name(1), 'Mercury')


# Assert
run_test()
