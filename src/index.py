# Libs
from pandas import DataFrame
from datetime import datetime, timedelta

from models.sheetModel import SheetModel

# Data
path = './resumo_fev.xls'
month_limit = 2  # Define the max month to check
money = 0


# Functions
def datasheet_to_json(dt: DataFrame) -> dict[str, float]:
    '''
        A method to set the days as key, and sum the values.
    '''
    # Create the json
    json: dict[str, float] = {}
    for line in dt.__array__():
        # Check if the date was datetime
        try:
            datetime.strptime(line[0], '%d/%m/%Y')
        except TypeError:
            line[0] = line[0].strftime('%d/%m/%Y')

        if (line[0].find(':') != -1):
            line[0] = str(line[0][:-9])

        if (line[0] in json):
            json[line[0]] += line[1]
            json[line[0]] = round(json[line[0]], 2)
            continue
        json[line[0]] = round(line[1], 2)

    return json


# Code
to_pay = SheetModel(path, 'Pagar')
to_receive = SheetModel(path, 'Receber')

to_pay_json = datasheet_to_json(to_pay.get_df())
to_receive_json = datasheet_to_json(to_receive.get_df())

# Go to all days from the month.
month = datetime(2023, 2, 1)

# Create the DataFrame
lines = []
for day in range(31):
    line = []

    # Check if the month has already anded.
    month += timedelta(1)
    current_day = month.strftime("%d/%m/%Y")
    line.append(current_day)
    if (month.month != month_limit):
        print('Month ended.')
        break

    # Remove the money from the day.
    removed = 0
    if (current_day in to_pay_json):
        removed = to_pay_json[current_day]

    money -= removed
    line.append(removed * -1)

    # Add the money
    added = 0
    if (current_day in to_receive_json):
        added = to_receive_json[current_day]

    money += added
    line.append(added)

    # Add the line to the lines
    line.append(money)
    lines.append(line)

print(lines)
dt = DataFrame(lines, columns=['Data', 'Retirado', 'Adicionado', 'total'])
print(dt)
