'''https://github.com/IgorOliveira42/StatusPlanilhaCSV'''
import re
import glob
import os
import pandas as pd

BASE_DIR = '.'
files = glob.glob(os.path.join(BASE_DIR, '*.csv'))


def verify_signal_from_csv(signal):
    '''
    This function is responsible to store the filtered value of signal
    in float_value var and return a string based on a condition.
    @param: signal Value of signal column.
    '''
    try:
        float_value = float(re.findall(r"-?\d+(?:\.\d+)?", signal)[0])
        return "SINAL BOM" if float_value > -29 else "SINAL RUIM"
    except KeyError:
        return None


def fill_status_in_file_lines(file):
    '''
    This function is responsible to read a csv file, check if column
    Status is present, create if not, and write Status value at
    respective column.
    @param: file CSV File
    '''
    read_csv = pd.read_csv(file, header=1)

    if 'Status' not in read_csv.columns:
        read_csv.insert(read_csv.columns.get_loc('Sinal') + 1, 'Status', None)

    read_csv['Status'] = read_csv['Sinal'].apply(verify_signal_from_csv)
    read_csv.to_csv(file, index=False)


def main():
    '''
    This function is responsible to execute the function below inside
    a for loop that iterate over files .csv present in local directory.
    '''
    for file in files:
        fill_status_in_file_lines(file)


if __name__ == '__main__':
    main()
