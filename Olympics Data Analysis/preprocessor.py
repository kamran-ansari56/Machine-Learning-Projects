import pandas as pd

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

def preprocess():
    global df, region_df

    # Filter only Summer season
    df = df[df['Season'] == 'Summer']

    # Merge region info
    df = df.merge(region_df, on='NOC', how='left')

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # One-hot encode Medal column
    df = pd.concat([df, pd.get_dummies(df['Medal'], prefix='Medal')], axis=1)

    return df
