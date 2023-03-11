import ru_local as ru

volume_gal = float(input(ru.VOLUMEINPUT))
volume_lit = volume_gal * 3.79
bbl_of_oil = volume_gal / 19.5
carbon_dioxide = volume_gal * 20
ethanol_volume = (volume_gal * 115000) / 75700
cost_usd = volume_gal * 3
avg_consume = 0.933
population_nsk = 1621500
population_rus = 145478097
city_consume = avg_consume * population_nsk
country_consume = avg_consume * population_rus * 365
print(ru.VOLUMEINLITRESOUTPUT, volume_lit)
print(ru.OILBARRELS, round(bbl_of_oil, 2))
print(ru.CARBONDIOXIDEOUTPTUT, round(carbon_dioxide, 2))
print(ru.ETHANOLOUTPUT, round(ethanol_volume, 2))
print(ru.COSTOUTPUT, cost_usd)
print(ru.CITYCONSUMEOUTPUT, round(city_consume, 2))
print(ru.COUNTRYCONSUMEOUTPUT, round(country_consume, 2))