planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name'))

# Muestra Earth

# planet['name'] es idéntico a usar planet.get('name')
print(planet['name'])

# Muestra Earth

wibble = planet.get('wibble') # Regresa None
print(wibble)
# wibble = planet['wibble'] # Arroja un KeyError

planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'

# name is now set to Makemake
print(planet['name'])

# name ahora es Makemake

# Usando update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Usando corchetes
planet['name'] = 'Jupiter'
planet['moons'] = 79

print(planet)

planet['orbital period'] = 4333

# el diccionario planet ahora contiene: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

planet.pop('orbital period')

# el diccionario planet ahora contiene: {
#   name: 'jupiter'
#   moons: 79
# }

# Añadimos los datos
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# el diccionario planet ahora contiene: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

print(f"""{planet['name']} polar diameter: {planet['diameter (km)']['polar']}""")

# Salida: Jupiter polar diameter: 133709

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Salida:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm

# El valor de december: 2.1cm

# Si, 'december' existe en rainfall
if 'december' in rainfall:
    # rainfall [en la posición december] es igual a
    # rainfall [en la posición december] + 1 (2.1+1)
    rainfall['december'] = rainfall['december'] + 1

# Si no:
else:

    # rainfall [en la posición december] es igual a 1
    rainfall['december'] = 1

# Como december si existe, el valor será 3.1

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

#Total de precipitaciones 0
total_rainfall = 0

# Para cada valor en los valores de rainfall
for value in rainfall.values():
    
    # El total de las precipitaciones será igual a ese mismo + el valor que se está iterando

    total_rainfall = total_rainfall + value

# Muestra 'Hay un total de precipitaciones (el valor total) en centímetros en el último cuarto (haciendo referencia al cuarto del año)

print(f'There was {total_rainfall}cm in the last quarter')

# Salida:
# There was 10.8cm in the last quarter