import pandas as pd

def load_data():
    file_path = 'data/sample_data.csv'
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    data = load_data()
    print(data.head())