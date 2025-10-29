
import argparse
import ast
import pandas as pd


def parse_release_date(x):
   
    try:
        return pd.to_datetime(x, errors='coerce')
    except Exception:
        return pd.NaT


def extract_num_votes_and_rating(df: pd.DataFrame) -> pd.DataFrame:

    if 'vote_average' in df.columns and 'vote_count' in df.columns:
        df['vote_average'] = pd.to_numeric(df['vote_average'], errors='coerce')
        df['vote_count'] = pd.to_numeric(df['vote_count'], errors='coerce')
    return df


def extract_genres(df: pd.DataFrame) -> pd.DataFrame:

    if 'genres' in df.columns:
        def _parse(g):
            if pd.isna(g):
                return []
            try:
                if isinstance(g, str) and g.startswith('['):
                    parsed = ast.literal_eval(g)
                    return [d.get('name') for d in parsed if isinstance(d, dict)]
            except Exception:
                return []
            return []
        df['genre_list'] = df['genres'].apply(_parse)
    return df


def main(input_path: str, output_path: str, sample: int | None = None):

    df = pd.read_csv(input_path, nrows=sample)


    df = extract_num_votes_and_rating(df)
    df = extract_genres(df)


    if 'release_date' in df.columns:
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
        df['release_year'] = df['release_date'].dt.year


    cols = []
    for c in [
        'id', 'title', 'original_title', 'release_date', 'release_year',
        'vote_average', 'vote_count', 'popularity', 'genre_list',
        'runtime', 'budget', 'revenue'
    ]:
        if c in df.columns:
            cols.append(c)

    summary = df[cols].copy()


    summary.to_csv(output_path, index=False)
    print(f"Saved summary to {output_path}. Rows: {len(summary)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input movie dataset CSV")
    parser.add_argument("--output", required=True, help="Path to save summary CSV")
    parser.add_argument("--sample", type=int, default=None, help="Read only N rows for testing")
    args = parser.parse_args()
    main(args.input, args.output, args.sample)
