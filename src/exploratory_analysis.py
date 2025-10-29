"""Generate common EDA charts: distribution of ratings, top genres, runtime vs rating, release-year trends."""
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os




def plot_rating_distribution(df, outdir):
    plt.figure()
    sns.histplot(df['vote_average'].dropna(), bins=30)
    plt.title('Rating distribution')
    plt.xlabel('Vote average')
    plt.savefig(os.path.join(outdir, 'rating_distribution.png'))
    plt.close()




def top_genres(df, outdir, top_n=10):
# explode genre_list
    g = df[['genre_list']].explode('genre_list')
    g = g['genre_list'].value_counts().head(top_n)
    plt.figure()
    g.plot(kind='bar')
    plt.title('Top genres')
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, 'top_genres.png'))
    plt.close()




def runtime_vs_rating(df, outdir):
    plt.figure()
    sns.scatterplot(x='runtime', y='vote_average', data=df)
    plt.title('Runtime vs Rating')
    plt.savefig(os.path.join(outdir, 'runtime_vs_rating.png'))
    plt.close()




def release_trend(df, outdir):
    s = df.groupby('release_year').size()
    plt.figure(figsize=(10,4))
    s.plot()
    plt.title('Movies per year')
    plt.savefig(os.path.join(outdir, 'movies_per_year.png'))
    plt.close()




def main(input_path, outdir):
    os.makedirs(outdir, exist_ok=True)
    df = pd.read_csv(input_path)
    plot_rating_distribution(df, outdir)
    top_genres(df, outdir)
    runtime_vs_rating(df, outdir)
    release_trend(df, outdir)
    print('Saved charts to', outdir)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--outdir', required=True)
    args = parser.parse_args()
    main(args.input, args.outdir)
