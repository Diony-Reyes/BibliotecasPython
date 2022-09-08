countryList = input("Inserte los países (separados por comas): ")
countryList = countryList.split(", ")
countryList = set(countryList)
countryList = list(countryList)
countryList.sort(reverse=False)
print(countryList)

# Qatar, España, Rusia, España, Afganistan
