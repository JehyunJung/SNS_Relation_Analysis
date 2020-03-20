from twitter_crawler import Twitter_Crawler
import sys

def synchronizer(keyword,pages=50):
    twitter_api=Twitter_Crawler()
    twitter_api.crawl_by_keyword(keyword,pages)

if __name__ =="__main__":
    if len(sys.argv) < 2:
        print('Wrong Execution')
        print('Try python ./data_synchronizer -k <keyword> -p <pages>[default page option is 50]')
    elif sys.argv[1]=='-k':
        if len(sys.argv)>2 :
            keyword=sys.argv[2]
            if sys.argv[3]=='-p':
                if len(sys.argv)>4:
                    pages=int(sys.argv[4])
                    synchronizer(keyword,pages)
                else:
                    print('page is not inserted')
            else:
                synchronizer(keyword)
        else:
            print('Keyword not inserted')

    else:
        print('Wrong option')
