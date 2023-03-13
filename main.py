import ru_local as ru

volume_gal = float(input(ru.VOLUMEINPUT))

volume_lit = volume_gal * 3.79
cost_usd = volume_gal * 3

# Number of oil barrels to produce that volume of gasoline.
bbl_of_oil = volume_gal / 19.5

# Volume of carbon dioxide while burning gasoline in engine in pounds.
carbon_dioxide = volume_gal * 20

# Equivalent volume of ethanol in gallons.
ethanol_volume = (volume_gal * 115000) / 75700

AVG_CONSUME = 0.933
POPULATION_NSK = 1621500
POPULATION_RUS = 145478097

# Gasoline consumption in liters for Novosibirsk per day.
city_consume = AVG_CONSUME * POPULATION_NSK

# Gasoline consumption in liters for Russia per year.
country_consume = AVG_CONSUME * POPULATION_RUS * 365

print(ru.VOLUMEOUTPUT, round(volume_lit, 2))
print(ru.OILBARRELS, round(bbl_of_oil, 2))
print(ru.CARBONDIOXIDEOUTPTUT, round(carbon_dioxide, 2))
print(ru.ETHANOLOUTPUT, round(ethanol_volume, 2))
print(ru.COSTOUTPUT, cost_usd)
print(ru.CITYCONSUMEOUTPUT, round(city_consume, 2))
print(ru.COUNTRYCONSUMEOUTPUT, round(country_consume, 2))