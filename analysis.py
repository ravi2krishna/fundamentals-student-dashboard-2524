# Data Analysis Related Functions (will use Pandas)

# Pandas - Pandas is a Python library that provides extensive means for data analysis. Data scientists often work with data stored in table formats like .csv,

import pandas as pd
import matplotlib.pyplot as plt

def load_students(path):
    return pd.read_csv(path)

def compute_summary(df):
    # add average column
    df['average'] = df[['math', 'science', 'english']].mean(axis=1)

    overall_avg = round(df['average'].mean(), 2)
    pass_condition = (df['math'] >= 40) & (df['science'] >= 40) & (df['english'] >= 40)
    pass_rate = round(100 * pass_condition.mean(), 2)

    per_stream = df.groupby('stream')[['math', 'science', 'english', 'average']].mean().round(2).to_dict(orient='index')
    top_students = df.sort_values('average', ascending=False).head(3)[['id','name','stream','average']].to_dict(orient='records')

    # save a simple bar chart to data/avg_by_stream.png
    plot_avg_by_stream(df)

    return {
        'overall_avg': overall_avg,
        'pass_rate_percent': pass_rate,
        'per_stream_avg': per_stream,
        'top_students': top_students
    }

def plot_avg_by_stream(df, outpath='data/avg_by_stream.png'):
    agg = df.groupby('stream')[['math','science','english']].mean().mean(axis=1)
    # single plot per tool rules: use matplotlib default colors
    plt.figure()
    agg.plot(kind='bar')
    plt.title('Average score by stream')
    plt.ylabel('Average')
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()