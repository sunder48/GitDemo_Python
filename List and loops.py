countries=["India","US","UK","Iran","Iraq","Aust"]
Counter=0
output=[]
for country in countries:
    if country.startswith('I'):
        Counter=Counter+1
        output.append(country)
print(output)
print(Counter)