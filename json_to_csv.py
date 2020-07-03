import pandas as pd
df = pd.read_json ('profile_posts_data.json')
df.to_csv ('profile_posts_data.csv', sep=',')