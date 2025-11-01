import pandas as pd
from config import CSV_PATH, THRESHOLD_YEARS_EXPERIENCE

def load_data():
    """
    Load data from the CSV file specified in config.

    Reads the CSV file, strips whitespace from column names to avoid issues,
    prints the list of columns, and returns the DataFrame.

    Returns:
        pd.DataFrame: The loaded DataFrame with cleaned column names.
    """
    df = pd.read_csv(CSV_PATH)
    # strip whitespace from column names to avoid issues
    df.columns = df.columns.str.strip()
    print("Columns in dataset:", df.columns.tolist())
    return df

def filter_by_experience(df):
    """
    Filter the DataFrame to include only rows where years of experience exceed the threshold.

    Args:
        df (pd.DataFrame): The input DataFrame containing the dataset.

    Returns:
        pd.DataFrame: The filtered DataFrame with rows where 'YearsExperience' > THRESHOLD_YEARS_EXPERIENCE.

    Raises:
        ValueError: If the 'YearsExperience' column is not found in the DataFrame.
    """
    col = 'YearsExperience'
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in dataset. Available columns: {', '.join(df.columns)}")
    filtered = df[df[col] > THRESHOLD_YEARS_EXPERIENCE]
    return filtered

def main():
    """
    Main function to execute the data loading and filtering process.

    Loads the data from the CSV file, filters it by experience threshold,
    and prints the first few rows of the filtered data. Handles any ValueError
    that may occur during filtering.
    """
    data = load_data()
    try:
        filtered_data = filter_by_experience(data)
        print(filtered_data.head())
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
