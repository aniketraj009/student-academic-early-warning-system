
import os
import pandas as pd

# ==========================================
# 1. CONFIGURATION
# ==========================================

DATA_PATH = "data/student-mat.csv"


# ==========================================
# 2. LOAD DATASET
# ==========================================

def load_data():

    print("\nLoading Dataset...")

    if not os.path.exists(DATA_PATH):

        raise FileNotFoundError(
            "Dataset not found in data folder"
        )

    df = pd.read_csv(DATA_PATH)

    print("\nDataset Loaded Successfully!")

    return df


# ==========================================
# 3. DATASET SHAPE
# ==========================================

def dataset_shape(df):

    print("\nDataset Shape:")

    print(df.shape)

    print("\nTotal Rows:")

    print(df.shape[0])

    print("\nTotal Columns:")

    print(df.shape[1])


# ==========================================
# 4. COLUMN NAMES
# ==========================================

def column_names(df):

    print("\nDataset Columns:")

    print(df.columns.tolist())


# ==========================================
# 5. DATA TYPES
# ==========================================

def data_types(df):

    print("\nData Types:")

    print(df.dtypes)


# ==========================================
# 6. FIRST 5 ROWS
# ==========================================

def first_rows(df):

    print("\nFirst 5 Rows:")

    print(df.head())


# ==========================================
# 7. MISSING VALUES
# ==========================================

def missing_values(df):

    print("\nMissing Values:")

    print(df.isnull().sum())

    print("\nTotal Missing Values:")

    print(df.isnull().sum().sum())


# ==========================================
# 8. MAIN EXECUTION
# ==========================================

def main():

    df = load_data()

    dataset_shape(df)

    column_names(df)

    data_types(df)

    first_rows(df)

    missing_values(df)


if __name__ == "__main__":

    main()
