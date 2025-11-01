import pandas as pd
from abc import ABC, abstractmethod

class DataTransform(ABC):
    @abstractmethod
    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


class NormalizeColumns(DataTransform):
    def apply(self, df):
        print("📏 Normalizing column names...")
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        return df


class RemoveDuplicates(DataTransform):
    def apply(self, df):
        print("🗑️ Removing duplicate rows...")
        return df.drop_duplicates()


class StandardizeText(DataTransform):
    def apply(self, df):
        print("🔤 Standardizing text to lowercase...")
        return df.applymap(lambda x: x.lower() if isinstance(x, str) else x)


class TransformFactory:
    @staticmethod
    def get_transform(transform_name):
        transforms = {
            "normalize": NormalizeColumns(),
            "remove_duplicates": RemoveDuplicates(),
            "standardize_text": StandardizeText()
        }
        return transforms.get(transform_name, None)


if __name__ == "__main__":
    df = pd.read_csv("sample_data.csv")
    transform = TransformFactory.get_transform("normalize")
    if transform:
        df = transform.apply(df)
    print(df.head())
