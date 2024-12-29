# House Price Predictor - Initial Version
# Author: Himal Kunwar
# Date: December 28, 2024

import pandas as pd
import numpy as np

# Create initial dataset
def create_dataset():
    return pd.DataFrame({
        'house_size': [1400, 1600, 1700, 1875, 1100],
        'bedrooms': [3, 3, 4, 4, 2],
        'location_score': [8, 7, 8, 9, 6],
        'price': [245000, 312000, 279000, 308000, 199000]
    })

# Analyze the dataset
def analyze_data(df):
    print("\nData Overview:")
    print("-" * 50)
    print(df.head())
    
    print("\nBasic Statistics:")
    print("-" * 50)
    print(df.describe())
    
    print("\nKey Insights:")
    print("-" * 50)
    print(f"Average price: ${df['price'].mean():,.2f}")
    print(f"Price range: ${df['price'].min():,.2f} - ${df['price'].max():,.2f}")

def main():
    # Create and analyze dataset
    df = create_dataset()
    analyze_data(df)

if __name__ == "__main__":
    main()
