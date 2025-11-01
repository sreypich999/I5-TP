import pandas as pd

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read(self):
        """Load the CSV file."""
        self.data = pd.read_csv(self.file_path)
        print("✅ CSV loaded successfully.")
        return self.data

    def preview(self, n=5):
        """Show the top n rows."""
        if self.data is None:
            print("⚠️ No data loaded. Call read() first.")
        else:
            print(self.data.head(n))


if __name__ == "__main__":
    reader = CSVReader("sample_data.csv")
    df = reader.read()
    reader.preview(5)
