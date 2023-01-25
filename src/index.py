# Libs
from pandas import DataFrame
from datetime import datetime, timedelta

from models.sheet_model import SheetModel
from models.config_model import ConfigModel

# Data
money = ConfigModel.get('OPTIONS', 'default_money', 0)
month_to_check = ConfigModel.get('OPTIONS', 'month_to_check')
dt = datetime(datetime.now().year, month_to_check, 1)

# Code
to_pay = SheetModel('To pay')
to_receive = SheetModel('To Receive')

# Create the DataFrame
df_arr = []
while (dt.month == month_to_check):
    line = []

    # Add the day to the line
    current_day = dt.strftime("%d/%m/%Y")
    line.append(current_day)

    # Remove the money from the day.
    removed = to_pay.get_day(current_day)[1]

    money -= removed
    line.append(removed)

    # Add the money
    added = to_receive.get_day(current_day)[1]
    money += added
    line.append(added)

    # Add the line to the lines
    line.append(money)
    df_arr.append(line)

    dt += timedelta(1)

df = DataFrame(df_arr, columns=['Date', 'Withdrawn', 'Added', 'Total'])
df.to_excel('result.xlsx', 'result', index=False)
