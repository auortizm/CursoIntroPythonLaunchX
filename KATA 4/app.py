fact = 'The Moon has no atmosphere.'
fact + 'No sound can be heard on the Moon.'
two_facts = fact + 'No sound can be heard on the Moon.'
two_facts

fact_Moon = """We only see about 60 of the Moon's surface, this is known as the "near side"."""


temperatures = 'Mars Average Temperature: -60 C'
print(temperatures .split(':'))

mars_temperature = 'The highest temperature on Mars is about 30 C'

for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

print('-60'.startswith('-'))

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

moon_facts = ['The Moon is drifting away from the Earth.',
              'On average, the Moon is moving about 4cm every year']
print('\n'.join(moon_facts))
mass_percentage = '1/6'
print('On the Moon, you would weigh about %s of your weight on Earth' %
      mass_percentage)

print("""Both sides of the %s get the same amount of sunlight,
    but only one side is seen from %s because
    the %s rotates around its own axis when it orbits %s.""" % ('Moon', 'Earth', 'Moon', 'Earth'))

mass_percentage = '1/6'
print('On the Moon, you would weigh about {} of your weight on Earth'.format(
    mass_percentage))
print(round(100/6, 1))