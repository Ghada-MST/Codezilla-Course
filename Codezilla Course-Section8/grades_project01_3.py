

country_name = input('Enter country name: ').lower().strip()

countries_fri_sat = ['egypt','ksa','saudi arabia''kuwait']
countries_sat_sun = ['usa','united states','uk','united kingdom','france']

if country_name in countries_fri_sat:
  print(f'Friday and Saturday are the weekends in {country_name.title()}')

elif country_name in countries_sat_sun:
  print(f'Saturday and Sunday are the weekends in {country_name.title()}')
  
else:
  print("Sorry,I don't know")
