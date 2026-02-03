# 20_city_names.py

# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like
# this:

# "Santiago, Chile"

# Call your function with at least three city-country pairs, and print the
# values that are returned.

def city_country(city, country):
  """Return a formatted string about a city and country."""
  formatted_string = f"{city.title()}, {country.title()}"
  return formatted_string

city_country_1 = city_country('tokyo', 'japan')
city_country_2 = city_country('seoul', 'south korea')
city_country_3 = city_country('beijing', 'china')
print(city_country_1)
print(city_country_2)
print(city_country_3)
