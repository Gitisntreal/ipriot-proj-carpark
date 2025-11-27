import unittest
import sys, os
from pathlib import Path

cwd = Path(os.path.dirname(__file__))
parent = str(cwd.parent)
sys.path.append(parent)

from smartpark.carpark_manager import CarparkManager
from smartpark.interfaces import CarparkDataProvider, CarparkSensorListener

class TestCarparkManagerInterface(unittest.TestCase):
    """
    Tests CarparkManager on the interface behaviour.
    """
    def setUp(self):
        self.manager = CarparkManager(location = ' Test Lot', total_spaces = 20)

    
    def test_is_instance_of_interfaces(self):
        """ 
        The CarparkManager should be implementing listener and data provider interfaces.
        """
        print('\n[Test] CarparkManager')
        print(f'Object type: {type(self.manager)}')
        print('Expexted results: CarparkDataProvider and CarparkSensorListener')
        
        actual_provider = isinstance(self.manager, CarparkDataProvider)
        actual_listener = isinstance(self.manager, CarparkSensorListener)

        print(f'Results: Provider={actual_provider}, Listener={actual_listener}')
        
        self.assertIsInstance(self.manager, CarparkDataProvider)
        self.assertIsInstance(self.manager, CarparkSensorListener)
    
    
    def test_temp_update_via_set_temp(self):
        """ 
        set_temperature() update the temperature property used by the display.
        """
        self.manager.set_temperature(23.5)
        results = self.manager.set_temperature
        print(f'Temperature set to:{results}')
        print('Expected results: 23.5')
        print(f'Manager temperature property is now: {self.manager.temperature}')
        
        self.assertAlmostEqual(self.manager.temperature, 23.5, places = 2)
        
if __name__ == "__main__":
    unittest.main()

# For this file to work you need to go into the carpark_manager and change the from interface to from smartpark.interface