import pandas as pd
from pathlib import Path
import re
import matplotlib.pyplot as plt



def load_data():
    file_path = 'C:\\Users\\MacRaeDC\\OneDrive - UMCG\\Documenten\\introduction_to_git_github\\data\\data.csv'
    df = pd.read_csv(file_path)
    return df






# THIS IS A SCRIPT TO PERFORM BASIC DATA ANALYSIS

if __name__ == "__main__":
    data = load_data()
    print("Data loaded successfully.")

    columns_of_interest = ['value', 'category']

    # Prepare dataframe
    df = data[columns_of_interest].copy()
    df['value'] = pd.to_numeric(df['value'], errors='coerce')  # ensure numeric
    df = df.dropna(subset=['value', 'category'])

