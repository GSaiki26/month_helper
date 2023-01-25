# Libs
from pandas import read_excel, DataFrame


# Classes
class SheetModel:
    def __init__(self, path: str, sheet: str):
        self.path = path
        self.sheet = sheet
        self.table = read_excel(
            path, sheet, engine='openpyxl')

    def get_df(self) -> DataFrame:
        '''
            A method to get an especific month from the sheet.
        '''
        return self.table
