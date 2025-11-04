import pandas as pd

def load_data():
    file_path = 'C:\\Users\\MacRaeDC\\OneDrive - UMCG\\Documenten\\introduction_to_git_github\\data\\data.csv'
    df = pd.read_csv(file_path)
    return df



def compute_mean_and_std(df, column):
    try:
        mean = df[column].mean()
        std = df[column].std()
    except Exception as e:
        mean = None
        std = None
    return mean, std



# THIS IS A SCRIPT TO PERFORM BASIC DATA ANALYSIS

if __name__ == "__main__":
    data = load_data()
    print("Data loaded successfully.")

    columns_of_interest = ['value', 'category']
    df_summary = []

    for column in columns_of_interest:
        mean, std = compute_mean_and_std(data, column)
        print(f"Mean: {mean}, Std: {std}")
        df_summary.append({'Column': column, 'Mean': mean, 'Std': std})

    df_summary = pd.DataFrame(df_summary)
    summary_file_path = 'C:\\Users\\MacRaeDC\\OneDrive - UMCG\\Documenten\\introduction_to_git_github\\outputs\\summary.csv'
    df_summary.to_csv(summary_file_path, index=False)

    
