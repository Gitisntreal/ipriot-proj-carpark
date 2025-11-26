import unittest
import sys,os
from pathlib import Path
cwd = Path(os.path.dirname(__file__))
parent = str(cwd.parent)

sys.path.append(parent + "/smartpark")

import configparser as pc

class TestConfigParsing(unittest.TestCase):

    def test_parse_config_has_correct_location_and_spaces(self):
        """
        The config "should" now provide location and total spaces. 
        """
        config_path = os.path.join(parent, 'samples_and_snippets', 'config.json')
        parking_lot = pc.parse_cofig(config_path)
        
        self.assertEqual(parking_lot['location'], 'moondalup')
        self.assertEqual(parking_lot['total-spaces'], 130)

# TODO: create an additional TestCase in a separate file with at least one test of the remaining classes. 

if __name__=="__main__":
    unittest.main()