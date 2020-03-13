import pandas as pd
from Preprocessor.data_preprocessor import Preprocessor
from relation_analyzer import Relation_Analyzer

def main():
    #twitter 데이터를 읽는다
    data=pd.read_csv('./data/twitter_data.csv')

    #데이터 내의 'text' column 전처리를 진행한다.
    Preprocessor.data_Preprocessing(data,'text')

    #전처리된 데이터를 이용해서 연관 분석을 진행한다.
    Relation_Analyzer.analyze(data['target'])

if __name__ == "__main__":
    main()