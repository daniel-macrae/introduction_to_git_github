import pandas as pd

def load_data():
    file_path = 'C:\\Users\\MacRaeDC\\OneDrive - UMCG\\Documenten\\introduction_to_git_github\\data\\data.csv'
    df = pd.read_csv(file_path)
    return df



def compute_mean_and_std(df, column):
    mean = df[column].mean()
    std = df[column].std()
    return mean, std


if __name__ == "__main__":
    data = load_data()
    print("Data loaded successfully.")

    columns_of_interest = ['value', 'category']

    for column in columns_of_interest:
        mean, std = compute_mean_and_std(data, column)
        print(f"Mean: {mean}, Std: {std}")

    
