from config_parser import parse_config
from carpark_manager import CarparkManager 


'''
    TODO: 
    - make your own module, or rename this one. Yours won't be a mock-up, so "mocks" is a bad name here. 
    - Read your configuration from a file. 
    - Write entries to a log file when something happens.
    - The "display" should update instantly when something happens
    - Make a "Car" class to contain information about cars:
        * License plate number. You can use this as an identifier
        * Entry time
        * Exit time
    - The manager class should record all activity. This includes:
        * Cars arriving
        * Cars departing
        * Temperature measurements.
    - The manager class should provide informtaion to potential customers:
        * The current time (optional)
        * The number of bays available
        * The current temperature
    
'''
def main() -> None:
    """A way to open the park management system"""
    config = parse_config('samples_and_snippets/config.json')
    location = config['location']
    total_spaces = config['total-spaces']
    manager = CarparkManager(location= location, total_spaces = total_spaces)
    
    print(f"Carpark: {location} ({total_spaces} spaces total)")
    print(f"Available spaces: {manager.available_spaces}")
    print(f"Current temperature: {manager.temperature}°C")
    print(f"Time: {manager.current_time}")
    

if __name__ == '__main__':
    main()

