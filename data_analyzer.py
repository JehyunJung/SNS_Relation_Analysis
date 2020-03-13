import pandas as pd
from Preprocessor.data_preprocessor import Preprocessor

def main():
    data=pd.read_csv('./data/twitter_data.csv')

    #데이터 내의 'text' column 전처리를 진행한다.
    data_preprocessor=Preprocessor()
    data_preprocessor.data_Preprocessing(data,'text')


if __name__ == "__main__":
    main()