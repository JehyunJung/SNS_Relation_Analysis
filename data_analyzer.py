import pandas as pd
import re
import konlpy.tag import Okt

#정규식을 이용해서 한글만을 남기도록 한다.
def korean_Extract(text):
    korean=re.compile('[^ ㄱ-ㅣ가-힣]+')
    result=korean.sub('',text)
    return result

#konlpy 패키지를 활용해서 명사(2글자 이상)만 남기도록 한다.
def noun_Extract(text):
    nouns_extractor=Okt()
    nouns=nouns_extractor.nouns(text)
    nouns=[noun for noun in nouns if len(noun) >1]
    return nouns
#Stopwords(불용어)를 제거하도록 한다.
def delete_Stopwords(text_data):
    stopwords=[]
    with open('./stopwords.txt', encoding='utf-8') as fp:
        stopwords=fp.readlines()
    stopwords=[stopword.strip() for stopword in stopwords]
    nouns=[text for text in text_data if text not in stopwords]
    return nouns

def data_Preprocessing(data):



def main():
    data=pd.read_csv('./data/twitter_data.csv')


if __name__ == "__main__":
    main()