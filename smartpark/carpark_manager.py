import logging
from datetime import datetime as dt
from interfaces import CarparkSensorListener, CarparkDataProvider

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

    def __init__(self, location: str, total_spaces: int) -> None:
        """ Create a new carpark manager.

        Args:
        location (str):  location of the carpark.
        total_space (int): The total number of spaces.
        
    """
        self._location = location
        self._total_spaces = int(total_spaces)
        self._temperature = 0.0
        self._cars_in_park = 0
        self._cars = set()

        logging.info(
            'CarparkManager created for "%s" with %s total space',
            self._location,
            self._total_spaces,
        )

    # Implementing CarparkSensorLinstener 

    def car_enter(self, liscense_plate: str) -> None:
        """
        Senses and signals when a car has parked.
        """
        self._cars_in_park += 1
        if liscense_plate:
            self._cars.add(liscense_plate)
        
        logging.info(
            'Car entering: %s | cars in park: %s',
            liscense_plate,
            self._cars_in_park,
        )
    
    def car_exit(self, liscense_plate: str) -> None:
        """
        Senses and signals when a car has left the space.
        """
        if self._cars_in_park > 0:
            self._cars_in_park -= 1 
        if liscense_plate and liscense_plate in self._cars:
            self._cars.remove(liscense_plate)
        
        logging.info(
            'Car exiting: %s | cars in park: %s',
            liscense_plate,
            self._cars_in_park,
        )
    
    def temperature(self, reading: float) -> None:
        """
        Provides the temperature reading.
        """
        self._temperature = float(reading)
        logging.info('Temperature updated: %.2f°C', self._temperature)

# Implementing CarperkDataProvider 

    @property
    def available_spaces(self) -> int:
        """ should show the amount of space left (if it in negative something is wrong)."""
        space_available = self._total_spaces - self._cars_in_park
        return max(space_available, 0)

    @property
    def temperature(self) -> float:
        """ should show the current temperature"""
        return self._temperature

    @property
    def current_time(self) -> str:
        """ Should show the current time as HH:MM:SS in display"""
        return dt.now().strftime('%H:%M:%S')
