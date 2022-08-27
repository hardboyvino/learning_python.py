def neat_city_name(city, country, population=None):
    """Returns a neatly formated city, country name."""
    if population:
        formated_place = f"{city.title()}, {country.title()} - population {population}"
        return formated_place
    else:
        formated_place = f"{city.title()}, {country.title()}"
        return formated_place
