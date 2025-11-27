import unittest
import sys ,os
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
        total_spaces = 1000
        manager = CarparkManager(location = 'Test Lot', total_spaces = total_spaces)
        acutal = manager.available_spaces
        
        print('Expected results: 1000')
        print(f'Results:{acutal}')
        
        self.assertEqual(1000, manager.available_spaces)
    
    def test_enter_exit_car(self):
        """
        This should test entering and exiting cars in which should adjust available spaces correctly.
        """
        manager = CarparkManager(location = 'Test Lot', total_spaces = 10)
       
        manager.car_enter('TJN-449')
        
        actual_first = manager.available_spaces
        
        print('Expected results 1 car entering: 9')
        print(f'Results: {actual_first}')
        
        self.assertEqual(9, manager.available_spaces)
        
        manager.car_enter('SKK-078')
        
        actual_second = manager.available_spaces
        
        print('Expected results 1 car entering: 8')
        print(f'Results: {actual_second}')
        
        self.assertEqual(8, manager.available_spaces)
       
        manager.car_enter('NXI-228')
        
        actual_third = manager.available_spaces
        
        print('Expected results 1 car entering: 7')
        print(f'Results: {actual_third}')
        
        
        self.assertEqual(7, manager.available_spaces)
        
        manager.car_exit('TJN-449')
        
        actual_fourth = manager.available_spaces
        
        print('Expected results 1 car exiting: 8')
        print(f'Results: {actual_fourth}')
        
        self.assertEqual(8, manager.available_spaces)

if __name__ == '__main__':
    unittest.main()

        # For this file to work you need to go into the carpark_manager and change the from interface to from smartpark.interface