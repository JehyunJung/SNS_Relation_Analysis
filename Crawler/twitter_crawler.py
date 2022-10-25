import pandas as pd
import json
import tweepy

class Twitter_Crawler():
    #Twitter API를 사용하기 위해서, 키를 입력해서 twitter.api.API 객체를 생성한다.
    def __init__(self):
        with open('./Crawler/server_config.json', encoding='utf-8') as fp:
            configs=json.load(fp)
            self.consumer_key=configs['CONSUMER_KEY']
            self.consumer_secret=configs['CONSUMER_SECRET']
            self.access_token_key=configs['ACCESS_TOKEN_KEY']
            self.access_token_secret=configs['ACCESS_TOKEN_SECRET']
            self.bearer_token=configs['BEARER_TOKEN']
        self.client=tweepy.Client(bearer_token=self.bearer_token)
        

    def crawl_by_keyword(self,keyword,pages):
        columns = ['created', 'text']
        df = pd.DataFrame(columns=columns)
        try:
            for page in range(pages):
                tweets = self.client.search_recent_tweets(query=keyword,tweet_fields=["created_at","text"],max_results=pages)
                for tweet in tweets.data:
                    tweet_text = tweet.text
                    created = tweet.created_at
                    df = pd.concat([df,pd.DataFrame([[created,tweet_text]],columns=df.columns)])
                print(page+1,' : ',len(df))
        except Exception as e :
            print(e)
            print('error occured, crawling finishing')
        print('crawling finished')

        df.to_csv('./data/twitter_data.csv',index=False,encoding='utf-8')

