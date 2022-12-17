import pandas as pd

def get_length(filename: str) -> int:
  df = pd.read_csv(filename)
  return len(df)

if __name__ == "__main__":
  get_length('input.txt')
