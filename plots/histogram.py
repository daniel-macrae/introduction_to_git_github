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

    

    # Output directory for plots

    # Overall distribution
    plt.figure(figsize=(8, 6))
    plt.hist(df['value'], bins=30, color='C0', edgecolor='black')
    plt.title('Distribution of value (overall)')
    plt.xlabel('value')
    plt.ylabel('Frequency')
    plt.tight_layout()
    overall_path =  'hist_value_overall.png'
    plt.savefig(overall_path)
    plt.close()
    print(f"Saved overall histogram: {overall_path}")

    
    # Distribution per category
    for cat, group in df.groupby('category'):
        plt.figure(figsize=(8, 6))
        plt.hist(group['value'], bins=30, color='C1', edgecolor='black')
        plt.title(f'Distribution of value — category: {cat}')
        plt.xlabel('value')
        plt.ylabel('Frequency')
        plt.tight_layout()
        path =  f"hist_value_category_{cat}.png"
        plt.close()
        
