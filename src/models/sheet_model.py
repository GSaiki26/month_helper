# Libs
from datetime import datetime

from pandas import read_excel
from models.config_model import ConfigModel


# Classes
class SheetModel:
    def __init__(self, sheet: str):
        self.path = ConfigModel.get('OPTIONS', 'file_path')
        self.sheet = sheet
        self.df = read_excel(
            self.path, self.sheet, engine='openpyxl')
        self.json = self.__to_json()

    def get_day(self, date: str) -> list[str, float]:
        '''
            A method to get the line from some day.
        '''
        return [date, self.json.get(date, 0.0)]

    def __to_json(self) -> dict[str, float]:
        '''
            A method to set the days as key, and sum the values.
        '''
        # Create the json
        json: dict[str, float] = {}
        for date, value in self.df.__array__():
            # Check if the date was datetime
            try:
                datetime.strptime(date, '%d/%m/%Y')
            except TypeError:
                date = date.strftime('%d/%m/%Y')

            # Add to the json
            if (date in json):
                json[date] += value
                json[date] = round(json[date], 2)
                continue

            # Round the value
            json[date] = round(value, 2)

        return json
