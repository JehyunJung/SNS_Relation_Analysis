from twitter_crawler import Twitter_Crawler

def synchronizer(**kwagrs):
    twitter_api=Twitter_Crawler()
    twitter_api.crawl_by_keyword(kwagrs['keyword'],kwagrs['pages'])

if __name__ =="__main__":
    synchronizer(keyword='손흥민',pages=10)
