countries = []
value  = True
country = input("Enter the country: ")
while value == True:
    countries.append(country.capitalize())
    value = False
print(countries)