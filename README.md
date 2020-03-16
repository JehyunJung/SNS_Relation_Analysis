# Twitter_Text_Analysis

## Description
'Twitter_Text_Analysis' 프로젝트는 SNS 데이터를 활용한 연관 분석 프로젝트입니다.

## Motivation
해당 프로젝트를 만들게 된 계기는 데이터 간에 가지는 **관계**를 파악하기 위해서입니다. 연관 분석을 통해, 어떠한 데이터끼리 자주 묶여서 쓰이는 지 확인 할 수 있습니다. 예를 들어, 아래와 같은 마트 구매 기록이 있다고 가정하자.

마트 방문일 | 구매 항목
---|:---:|
1일| 기저귀, 맥주, 우유
5일| 기저귀, 우유 , 빵, 버터, 맥주
10일| 맥주, 빵, 과자, 기저귀
15일| 맥주, 라면 , 기저귀, 우유
20일| 빵, 버터, 콜라, 과자, 우유

해당 표를 통해 알 수 있는 점은, [맥주, 기저귀], [빵, 버터], 등의 상품들이 서로 연관 되어 있는 것을 확인 할 수 있습니다. 이와 같은 데이터를 활용하여서 마트, 슈퍼, 등은 해당 제품들을 가까이 진열해놓게 되면, 고객들이 해당 제품들을 구매하므로써 이윤을 추구 할 있다.


## Contents 
1. 크롤링 모듈
    - 트위터 크롤러
    - 페이스북 크롤러(추가 예정...)
2. 데이터 전처리 과정 
    - 한글을 제외한 나머지 단어 제거
    - 불용어 제거
    - 명사 추출 
2. 워드클라우드 이미지
3. 연관 분석 결과(수정 필요...)

## Requirements
설치해야하는 패키지는 requirements.yml에 명시되어 있습니다.
- Anaconda3 -> conda environment
- matplotlib
- apyori
- konlpy
- networkx
- pytagcloud
- tweepy
- Java required
    - ubuntu 환경에서는 java를 아래의 명령어를 통해 간편하게 설치 할 수 있습니다.
    ```bash
    USER@LOCALHOST:*/SNS_Relation_Analysis$ sudo apt-get install openjdk-9-jre
    USER@LOCALHOST:*/SNS_Relation_Analysis$ sudo apt-get install openjdk-9-jdk
    ```
    - Google Cloud Platform 과 같이 headless한 서버를 사용하는 경우 아래의 명령어를 입력하면 됩니다.
    ```bash
    USER@LOCALHOST:*/SNS_Relation_Analysis$ sudo apt-get install openjdk-9-jre-headless
    USER@LOCALHOST:*/SNS_Relation_Analysis$ sudo apt-get install openjdk-9-jdk-headless
    ```
## How to run
1. requirement.yml을 이용해서 conda 가상환경을 설정합니다.
    ```bash
    USER@LOCALHOST:*/SNS_Relation_Analysis$ conda env create -f requirements.yml
    USER@LOCALHOST:*/SNS_Relation_Analysis$ conda activate DataAnalysis
    ```
2. pytagcloud(워드클라우드 관련 패키지)에서 한글을 출력하기 위해 한글을 지원하는 나눔고딕을 사용한다. 이를 위해, font 설정을 진행해야 한다.
    - 우선 해당 패키지의 fonts 폴더 경로를 알아야합니다.
        - 정상적으로 Anaconda3을 설치하셨다면 '~/anaconda3/envs/DataAnalysis/lib/python3.7/site-packages/pytagcloud/fonts/' 경로에 fonts 설정 파일이 존재해야합니다.
    - 그 후, Fonts/Nanumgothic.ttf 파일을 fonts 폴더에 복사해줍니다.
    - 이렇게 해도 동작하지 않는 경우에 대해서는,
    	```json
		{  
			"name": "NanumGothic",  
			"ttf": "NanumGothic.ttf",  
			"web": "http://fonts.googleapis.com/css?family=Nanum+Gothic"  
	    }
	```
	    
       위의 text config정보를 pytagcloud 패키지의 fonts.json에 추가해주도록 합니다.
    
3. 트위터 데이터를 얻기 위해서는 server_config.json에 자신의 API key를 등록해야 한다.
    - 해당 부분은  https://developer.twitter.com/en/apps 에서 트위터 개발자 회원 가입을 진행하면 됩니다.
    - server_config.json
    	```json 
		{  
    			"CONSUMER_KEY":"{YOUR_KEY}",  
    			"CONSUMER_SECRET":"{YOUR_KEY}",  
    			"ACCESS_TOKEN_KEY":"{YOUR_KEY}",  
    			"ACCESS_TOKEN_SECRET":"{YOUR_KEY}"  
		}
	```

4. Crawler/data_synchrnozier.py에 키워드,page 정보를 입력해줍니다. 
    - 아래와 같이 keyword, 크롤링할 page수를 등록해줍니다.
     ```python
        synchronizer(keyword='손흥민',pages=100)
     ```
    - 그런 다음, 해당 파이썬 파일을 실행해줍니다.

5. 마지막으로, relation_analyzer.py을 실행하면, Results 폴더 연관분석 결과가 추출됩니다.

## Results
<img src="./Results/wordcloud(Twitter).png" alt="wordcloud" width="300" height="300"/> 
<img src="./Relation_Analyzing_Result(Twitter).png" alt="wordcloud" width="300" height="300"/>
