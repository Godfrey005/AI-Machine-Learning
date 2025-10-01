import pandas as pd

def main():
    print("Fake News Detection Project")
    # Example: Load a CSV file (replace 'data/news.csv' with your actual dataset path)
    try:
        df = pd.read_csv("../data/news.csv")
        print("Loaded dataset:")
        print(df.head())
    except FileNotFoundError:
        print("Dataset not found. Add a CSV file to data/news.csv to continue.")

if __name__ == "__main__":
    main()
