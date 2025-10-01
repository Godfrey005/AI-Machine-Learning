import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_prepare_data(filepath):
    # Load data
    df = pd.read_csv(filepath)
    print(f"Loaded dataset with {len(df)} rows.")

    # Basic cleaning
    df = df.dropna()
    print(f"After removing NA: {len(df)} rows.")

    # Train-test split
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    print(f"Train size: {len(train)}, Test size: {len(test)}")

    # Save splits (optional)
    train.to_csv("../data/train.csv", index=False)
    test.to_csv("../data/test.csv", index=False)

    return train, test

if __name__ == "__main__":
    train, test = load_and_prepare_data("../data/news.csv")
