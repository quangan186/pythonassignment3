
from datetime import datetime
import time

# set time
start = "11/05/2021 00:00:00"
d = datetime.strptime(start, "%d/%m/%Y %H:%M:%S")
t0 = time.mktime(d.timetuple())
t1 = time.time()

# distance between Mars and Earth
s = 230000000  # km

# velocity of spaceship
v = 11.11  # km/s

delta_time_seconds = t1 - t0

# distance from Earth
distance_from_Earth = int(v * delta_time_seconds)
print(f'Current distance from spaceship to Earth: {distance_from_Earth} km')
distance_from_Mars = int(s - delta_time_seconds * v)

# distance from Mars
print(f'Current distance from spaceship to Mars: {distance_from_Mars} km')

# estimated time of arrival
estimate_time = ((s - v * delta_time_seconds) / v) / 3600  # hours
print(f'Estimated time of arrival: {estimate_time}')
