import pyowm

owm = pyowm.OWM('f62c09736de3a1383865a064652aebfd')


def is_city():
    try:
        own = owm.weather_at_place("ddsdava342189283dfdq942qipo2opiq2pionsadf")
        return "ayyee"
    except pyowm.exceptions.not_found_error.NotFoundError:
        return "dsiafdj"

print(is_city())
    