import time
import pandas as pd
from functools import wraps

# Decorators
def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Starting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"✅ Finished {func.__name__}.")
        return result
    return wrapper

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ Execution time for {func.__name__}: {end - start:.4f} seconds.")
        return result
    return wrapper


class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    @log_action
    @log_time
    def read(self):
        self.data = pd.read_csv(self.file_path)
        return self.data

    @log_action
    def preview(self, n=5):
        print(self.data.head(n))


if __name__ == "__main__":
    reader = CSVReader("sample_data.csv")
    df = reader.read()
    reader.preview(3)
