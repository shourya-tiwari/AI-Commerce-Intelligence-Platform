import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")


def audit_dataset(file_path):
    df = pd.read_csv(file_path)

    print("\n" + "=" * 50)
    print(file_path.name)
    print("=" * 50)

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicates:")
    print(df.duplicated().sum())


def main():

    for csv_file in RAW_DATA_PATH.glob("*.csv"):
        audit_dataset(csv_file)


if __name__ == "__main__":
    main()