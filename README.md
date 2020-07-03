# facebook-comment-scaping-preprocessing
How to use:
1) specify your facebook credentials in credential.json and the profile url of the profile you want to scrape in profiles_url.json
2) CLI command : python master_scraper.py

3)output of master_scraper is stored in profile_posts_data.json. if you want to convert it into csv formate then CLI command: python json_to_csv.py

4)profile_posts_data.csv is formed which you can now use for data preprocessing in NLP!!

5)tokenization, stop word removal, stemming and lammetization is done in preprocessing_pipeline.ipynb
