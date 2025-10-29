from typing import Tuple
import pandas as pd




def load_csv(path: str, nrows: int | None = None) -> pd.DataFrame:
    return pd.read_csv(path, nrows=nrows)




def save_df(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False)
