import pandas as pd

path='C:/Users/Ishika/cust-support-agent/data/raw/twcs.csv'
df = pd.read_csv(path)
spotify_df = df[df['author_id'] == 'SpotifyCares']
merged_df=pd.merge(spotify_df, df, left_on='in_response_to_tweet_id', right_on='tweet_id', how='left', suffixes=('_spotify', '_customer')   )

#to_convert=merged_df[['text_customer', 'text_spotify']]
header = ["text_spotify", "tweet_id_customer", "text_customer","in_response_to_tweet_id_customer"]

merged_df.dropna(how='all').to_csv('C:/Users/Ishika/cust-support-agent/data/processed/converted_df.csv', index=False, columns=header)