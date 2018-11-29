import pandas as pd

with open('9196-fulltext.txt', 'r') as file:
    text = file.read()
    text = str(text)
    text = text.replace('.','').split(' ')
    # text = 'aa vv sddd'

    df_csv = pd.read_csv('provincial.csv')

    index = df_csv.index.values

    cities = {}
    citiesCount = {}
    print(df_csv)
    for l in df_csv['s']:
        cities[l] = l.split()
        citiesCount[l] = 0
    found_match = False
    for word in text:
        if found_match:
            cityTest = cityTest
        else:
            cityTest = ''
        found_match = False
        # print(word)
        for city in cities.keys():
            # print(cities[city])
            # print(citiesCount[city])

            if word in cities[city]:
                cityTest += word + ' '
                found_match = True
            if cityTest.split(' ')[0:-1] == city.split(' '):
                print(city)
                citiesCount[city] += 1
                print(citiesCount[city])
    print(citiesCount)

            # if cityTest.split(' ')[0:-1] == city.split(' '):
            #     print (city)    #Print if it found a city.
