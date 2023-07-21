import re
import glob
import os
import pandas as pd

BASE_DIR = '.'
files = glob.glob(os.path.join(BASE_DIR, '*.csv'))

def verify_signal_from_csv(signal):
    try:
        float_value = float(re.findall(r"-?\d+(?:\.\d+)?", signal)[0])
        return "SINAL BOM" if float_value > -29 else "SINAL RUIM"
    except:
        return None


def fill_status_in_file_lines(file):
    df = pd.read_csv(file, header=1)
    
    if 'Status' not in df.columns:
        df.insert(df.columns.get_loc('Sinal') + 1, 'Status', None)

    df['Status'] = df['Sinal'].apply(verify_signal_from_csv)
    df.to_csv(file, index=False)


def main():
    for file in files:
        fill_status_in_file_lines(file)


if __name__ == '__main__':
    main()
