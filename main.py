travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# write the function that will allow new countries to be added to the travel_log. 👇
def add_new_country(countryVisited, timesVisited, citiesVisited):
    newCountry = {}
    newCountry['country'] = countryVisited
    newCountry['visits'] = timesVisited
    newCountry['cities'] = countryVisited
    travel_log.append(newCountry)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
