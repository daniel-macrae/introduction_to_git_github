import pandas as pd

def load_data():
    file_path = 'C:\\Users\\MacRaeDC\\OneDrive - UMCG\\Documenten\\introduction_to_git_github\\data\\data.csv'
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    data = load_data()
    print(data.head())