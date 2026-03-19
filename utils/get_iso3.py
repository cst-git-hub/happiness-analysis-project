import pycountry


def get_iso3(country_name):

    try:
        country = pycountry.countries.lookup(country_name)
        return country.alpha_3

    except LookupError:
        return None