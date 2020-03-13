import pandas as pd
import json
import tweepy

class Twitter_Crawler():
    #Twitter API를 사용하기 위해서, 키를 입력해서 twitter.api.API 객체를 생성한다.
    def __init__(self):
        with open('../server_config.json', encoding='utf-8') as fp:
            configs=json.load(fp)
            self.consumer_key=configs['CONSUMER_KEY']
            self.consumer_secret=configs['CONSUMER_SECRET']
            self.access_token_key=configs['ACCESS_TOKEN_KEY']
            self.access_token_secret=configs['ACCESS_TOKEN_SECRET']

        auth=tweepy.OAuthHandler(self.consumer_key,self.consumer_secret)
        auth.set_access_token(self.access_token_key,self.access_token_secret)
        self.api=tweepy.API(auth)

    def crawl_by_keyword(self,keyword,pages):
        columns = ['created', 'text']
        df = pd.DataFrame(columns=columns)

        try:
            for page in range(pages):
                tweets = self.api.search(keyword,count=100)

                for tweet in tweets:
                    tweet_text = tweet.text
                    created = tweet.created_at
                    row = [created, tweet_text]
                    series = pd.Series(row, index=df.columns)
                    df = df.append(series, ignore_index=True)
                print(page+1,' : ',len(df))
        except :
            print('error occured, crawling finishing')
        print('crawling finished')

        df.to_csv('../data/twitter_data.csv',index=False,encoding='utf-8')

