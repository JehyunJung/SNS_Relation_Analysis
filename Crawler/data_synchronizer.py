from Crawler.twitter_crawler import Twitter_Crawler

def synchronizer(**kwagrs):
    twitter_api=Twitter_Crawler()
    twitter_api.crawl_by_keyword(kwagrs['keyword'],kwagrs['pages'])

if __name__ =="__main__":
    synchronizer(keyword='코로나',pages=100)