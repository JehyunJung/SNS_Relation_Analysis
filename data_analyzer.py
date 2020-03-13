import pandas as pd
from Preprocessor.data_preprocessor import Preprocessor
from konlpy.tag import Okt

def main():
    data=pd.read_csv('./data/twitter_data.csv')


if __name__ == "__main__":
    main()