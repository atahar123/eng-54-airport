# do the simplest switchboard

from aircraft_class import *
from flights_class import *
from people_class import *
from passenger_class import *
import sys


print('==========Adding a plane==========')
planes_list = []
while True:
    cargo = input('Enter cargo size\n')
    plane = input('Enter plane name\n')
    plane_number = input('Enter plane number\n')
    newplane = Aircraft(cargo, plane)
    planes_list.append(newplane)

    print(f'PLane Name is {plane}. Cargo size is {cargo}. Plane number is {plane_number}')

    if cargo == 'Quit' or plane == 'Quit':
        break

print('==========Adding a passenger==========')
passenger_list = []
while True:
    p_name = input('Enter full passenger name\n')
    passport_number = input('Enter passport number\n')
    newpassenger = Passenger(p_name, passport_number)
    passenger_list.append(newpassenger)

    print(f'Passenger name is {p_name}. Passport number is {passport_number}')

    if p_name == 'Quit' or passport_number == 'Quit':
        break


print('==========Adding a flight==========')
flight_list = []
while True:
    plane = input('Enter plane\n')
    origin = input('Enter origin\n')
    plane_number = input('Enter plane number\n')
    destination = input('Enter destination\n')
    passengers = input('Enter amount of passengers\n')
    newflight = flight_trip(plane, origin, plane_number, destination)
    flight_list.append(newflight)

    print(f'PLane Name is {plane}. Origin is {origin}. Plane Number is {plane_number}. Destination is {destination}')

    if plane == 'Quit' or origin == 'Quit' or plane_number == 'Quit' or destination == 'Quit' or passengers == 'Quit':
        break
