import logging
from datetime import datetime as dt
from interfaces import CarparkSensorListener, CarparkDataProvider
#from smartpark.interfaces import CarparkSensorListener, CarparkDataProvider

logging.basicConfig(
    filename = 'carpark.log',
    level = logging.INFO,
    format =  '%(asctime)s %(levelname)s %(message)s'
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

    def car_enter(self, lp: str) -> None:
        """
        Senses and signals when a car has parked.
        """
        if not lp:
            return
        
        if lp in self._cars:
            logging.warning('Duplicate Entry Ignored: %s', lp)
            return
        
        if self._cars_in_park >= self._total_spaces:
            logging.warning('Carpark Is Full: Entry Is Denied: %2', lp)
            return
    
        car = Car(lp)
        car.entry_time = dt.now()
        car.exit_time = None
        
        self._cars.add(car)
        self._cars_in_park += 1 
        
        logging.info(
            'Car Entering: %s | Cars In Park: %s',
            lp,
            self._cars_in_park 
        )

    
    def car_exit(self, lp: str) -> None:
        """
        Senses and signals when a car has left the space.
        """
        if not lp:
            return
        
        if lp not in self._cars:
            logging.warning('Exit Ignored (Not Found): %s', lp)
            return
        
        car_object = next(c for c in self._cars if c == lp)
        car_object.exit_time = dt.now()
        
        self._cars.remove(car_object)
        self._cars_in_park -= 1 
        
        logging.info(
            'Car Exiting: %s | Cars In Park: %s',
            lp,
            self._cars_in_park 
        )

    
    def set_temperature(self, reading: float) -> None:
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

class Car:
    """ Represents a car by its license plate, entry/exit time, make/model. """
    def __init__(self,lp: str, make: str = '', model: str = '' ):
        self.lp = lp
        self.make = make 
        self.model = model
        self.entry_time = None 
        self.exit_time = None
    
    def __eq__(self, value):
        """Equality test for comparing cars by their license plates."""
        if type(value) == str:
            return self.lp == value
        elif type(value) == Car:
            return self.lp == value.lp
        else:
            return value is self
        
    def __hash__(self):
        """A hash code identifies an object for use in sets and dictionaries.
        Delegete the hash code to the license plate string."""
        return hash(self.lp)
    # To do  1. License Plate (Must hold the info - done ) 2. entry/exit time (done - should detect duplicates now when entering the lp among other things) 3. make/model ( as a place holder)