import pandas as pd
from abc import ABC, abstractmethod
#2. Abstract Base Class (ABC)
class MissingValueStrategy(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

# . Strategy Classes (Different ways to handle missing data)
class DropMissing(MissingValueStrategy):  # Inherits from MissingValueStrategy
    def handle(self, df):
        print("🧹 Dropping rows with missing values...")
        return df.dropna()


class FillMean(MissingValueStrategy):
    def handle(self, df):
        print("🧮 Filling missing numeric values with mean...")
        return df.fillna(df.mean(numeric_only=True))


class FillMode(MissingValueStrategy):
    def handle(self, df):
        print("🧩 Filling missing values with mode...")
        return df.fillna(df.mode().iloc[0])

# The DataCleaner class (uses strategy)
class DataCleaner:
    def __init__(self, strategy: MissingValueStrategy):
        self.strategy = strategy
# method
    def clean(self, df):
        return self.strategy.handle(df)


if __name__ == "__main__":
    df = pd.read_csv("sample_data.csv")
    cleaner = DataCleaner(FillMean())
    cleaned_df = cleaner.clean(df)
    print(cleaned_df.head())
