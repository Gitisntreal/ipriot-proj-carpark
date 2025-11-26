import unittest
import sys,os
from pathlib import Path
cwd = Path(os.path.dirname(__file__))
parent = str(cwd.parent)

sys.path.append(parent + "/smartpark")

#Change the line below to import your manager class
from carpark_manager import CarparkManager

class TestConfigParsing(unittest.TestCase):

    def test_fresh_carpark(self):
        carpark = CarparkManager(location = 'Test', total_space = 1000)
        self.assertEqual(1000,carpark.available_spaces)

if __name__=="__carpark_main__":
    unittest.main()
