# Libs
from json import loads
from configparser import ConfigParser

# Data
path = './config.conf'


# Classes
class ConfigModel:
    @staticmethod
    def get(section: str, key: str, default: any = None) -> any:
        '''
            A method to get some value from the config file.
        '''
        # Create the config parser and get the key.
        cp = ConfigParser()
        cp.read(path)
        value = cp.get(section, key)

        # Return
        return loads(value) if value else default
