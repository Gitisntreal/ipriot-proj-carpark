import unittest
import sys,os
from pathlib import Path

cwd = Path(os.path.dirname(__file__))
parent = str(cwd.parent)
sys.path.append(parent)

#Change the line below to import your manager class
from smartpark.carpark_manager import CarparkManager

class TestCarparkManager(unittest.TestCase):
    """ 
    Testing class for CarparkManager Behaviour.
    """
    def test_carpark_has_spaces(self):
        """
        This should test a fresh carpark having all avialable spaces.
        """
        manager = CarparkManager(location = 'Test Lot', total_spaces = 1000)
        self.assertEqual(1000, manager.available_spaces)
        
    def test_enter_exit_car(self):
        """
        This should test entering and exiting cars in which should adjust available spaces correctly.
        """
        manager = CarparkManager(location = 'Test Lot', total_spaces = 10)
       
        manager.car_enter('TJN-449')
        self.assertEqual(9, manager.available_spaces)
        
        manager.car_enter('SKK-078')
        self.assertEqual(8, manager.available_spaces)
       
        manager.car_enter('NXI-228')
        self.assertEqual(7, manager.available_spaces)
        
        manager.car_exit('TJN-449')
        self.assertEqual(8, manager.available_spaces)

if __name__ == '__main__':
    unittest.main()
        