# Defino mi función
from datetime import timedelta, datetime


def rocket_parts():
    return 'payload, propellant, structure'


output = rocket_parts()

print(output)

print(any([True, False, False]))
print(any([False, False, False]))
print(str(15))


def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'


print(distance_from_earth('Saturn'))


def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24


total_days = days_to_complete(238855, 75)

print(round(total_days))
print(round(days_to_complete(238855, 75)))


def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')


print(arrival_time('Earth'))

print(arrival_time('Orbit', hours=0.13))


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {total_minutes/60} hours'

print(sequence_time(60))


def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day='Wednesday', pilots=3)

print(variable_length)

def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')

crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', command_pilot='Michael Collins')