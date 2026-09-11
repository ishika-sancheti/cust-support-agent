import pandas as pd

path='C:/Users/Ishika/cust-support-agent/data/raw/twcs.csv'
df = pd.read_csv(path)
spotify_df = df[df['author_id'] == 'SpotifyCares']
merged_df=pd.merge(spotify_df, df, left_on='in_response_to_tweet_id', right_on='tweet_id', how='left', suffixes=('_spotify', '_customer')   )
print(merged_df[['text_customer', 'text_spotify']].head(10))
