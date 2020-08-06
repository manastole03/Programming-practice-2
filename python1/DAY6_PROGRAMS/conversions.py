# Python function that convert feet into inches.
def ft_to_inch(ft):
    inches = ('{:.2f}'.format(ft*12))
    print(f'{ft} feet = {inches} inches')
ft = float(input("Feet:  "))
ft_to_inch(ft)

# Python function to convert miles to kilimeter.
def miles_to_km(miles):
    km = ('{:.2f}'.format(miles/0.6214))
    print(f'{miles} miles = {km} kilometers')
miles = float(input("Miles:  "))
miles_to_km(miles)

# Python function to convert acre to square yards
def acre_to_sqyards(acres):
    sq_yards = ('{:.2f}'.format(acres*4840))
    print(f'{acres} acres = {sq_yards} square yards')
acres = float(input("Acres:  "))
acre_to_sqyards(acres)
