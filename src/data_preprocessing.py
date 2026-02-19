import pandas as pd

def clean_data(filepath):
    df = pd.read_csv(filepath)

    df = df[df['price'] > 0]
    df = df[df['sqft'] > 200]

    df.fillna({
        'bedrooms': df['bedrooms'].median(),
        'bathrooms': df['bathrooms'].median()
    }, inplace=True)

    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    clean_df = clean_data("data/raw/housing_raw.csv")
    clean_df.to_csv("data/processed/housing_clean.csv", index=False)
