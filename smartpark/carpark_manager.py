import logging
from datetime import datetime as dt
from smartpark.interfaces import CarparkSensorListener, CarparkDataProvider

logging.basicConfig(
    filename = 'carpark.log',
    level = logging.INFO,
    format =  '%(asctime)s%(levelname)s%(message)s'
)

class CarparkManager(CarparkSensorListener, CarparkDataProvider):
    """

    Carpark management state: where cars enters/exits, space aviability, temperature and time.
    implenmentation of both:
        - CarparkSensorListener (reacts to sensor events)
        - CarparkDataProvider (provide data to display)

    """

def __init__(self, location: str, total_space: int):
    self._location = location
    self._total_space = total_space
    self._temperature = 0.0
    self._cars_in_park = 0

# Implementing CarparkSensorLinstener 

def car_enter(self, temperature: float):
    """ calls when a car enter the car park"""
    self._cars_in_park += 1
    self._temperature = temperature
    logging.info('Car has entered. Cars in park: %s, temp: %s',
                 self._cars_in_park, self._temperature)
    
def car_exit(self, temperature: float):
    """ calls when a car exit the carpark"""
    if self._cars_in_park > 0:
        self._cars_in_park -= 1 
    self._temperature = temperature
    logging.info('Car has exited. Cars in park: %s, temp: %s',
                 self._cars_in_park, self._temperature)

# Implementing CarperkDataProvider 

@property
def available_spaces(self) -> int:
    """ should show the amount of space left (if it in negative something is wrong)."""
    space_available = self._total_space - self._cars_in_park
    return max(space_available, 0)

@property
def temperature(self) -> float:
    """ should show the temperature"""
    return self._temperature

@property
def current_time(self) -> str:
    """ Should show the current time as a string (allows to use of OCT/NOV/ DEC ect) in display"""
    return dt.now().strftime('%H:%M:%S')
