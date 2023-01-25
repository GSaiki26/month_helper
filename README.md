# Month Helper
The month helper application is a python-app created with the objective to show to the user all the money that he spend and earned within 1 month.

To use the application, you need to created a excel file (with the name can be provided in the ./data/config.conf) with 2 sheets, named "To pay" and "To receive".
In the sheets, the format need to be like:

|   Data    |   Value   |
|-----------|-----------|
|01/01/2023 |   12.00   |


## Config.conf
The `config.conf` is a file located in the data folder to keep the environments.
The keys from the file are:
- "`file_path`":
The input file path to be read.

* "`file_output`":
The output file path to be written.

* "`date_format`":
The date's format to be read in the input file. The format to be used is the same as datetime library.
Only tested using ``"%d/%m/%Y"`` (Brazilian date format)

* "`default_money`":
The value to be used in the start of the month.

* "`month_to_check`":
The month of the year to check.

* "`year_to_check`":
The year to be check.