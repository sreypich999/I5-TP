import pandas as pd
from abc import ABC, abstractmethod
from exercise1_csv_reader import CSVReader
from exercise2_missing_strategy import DataCleaner, FillMean
from exercise4_factory_pattern import TransformFactory


class DataPipeline(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def clean(self, df): pass

    @abstractmethod
    def transform(self, df): pass

    @abstractmethod
    def save(self, df): pass

    def run(self):
        df = self.load()
        df = self.clean(df)
        df = self.transform(df)
        self.save(df)
        print("🏁 Pipeline completed successfully!")


class CSVDataPipeline(DataPipeline):
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def load(self):
        reader = CSVReader(self.input_path)
        return reader.read()

    def clean(self, df):
        cleaner = DataCleaner(FillMean())
        return cleaner.clean(df)

    def transform(self, df):
        factory = TransformFactory()
        transform = factory.get_transform("normalize")
        if transform:
            df = transform.apply(df)
        return df

    def save(self, df):
        df.to_csv(self.output_path, index=False)
        print(f"💾 Saved cleaned data to: {self.output_path}")


if __name__ == "__main__":
    pipeline = CSVDataPipeline("sample_data.csv", "cleaned_data.csv")
    pipeline.run()
