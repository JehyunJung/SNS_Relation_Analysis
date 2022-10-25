from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from konlpy.tag import Okt
from collections import Counter
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import networkx as nx
import pytagcloud
import re
from os.path import dirname,join


class Association_Analyzer:
    @staticmethod
    def relation_analysis(data):
        #키워드 간에 연관성 분석을 진행한다.
        transactions=data['target'].tolist()
        transactions = [transaction for transaction in transactions if transaction]

        #각각의 리스트에 대해서 원소가 포함되어 있는 지 여부를 TransactionEncoder을 통해 나타낸다.
        transaction_encoder=TransactionEncoder()
        transactions=transaction_encoder.fit(transactions).transform(transactions)
        transactions_df=pd.DataFrame(transactions,columns=transaction_encoder.columns_)
        #지지도라고 하는 것은 전체 항목에서 x,y가 연관되어 있는 정도를 나타내는 것인데 이게 각 행에 대해 어느 정도 비율로 존재하는 지를 나타내는 수치이다.
        #이 수치가 높으면 높을 수록 두 개의 연과성이 높다는 것을 의미한다.
        results=apriori(transactions_df, min_support=0.1, max_len=2,use_colnames=True)

        #노드 2개가 서로 연결되어 있는 구조를 추출한다.
        columns=['source','target','weight']
        keyword_network=pd.DataFrame(columns=columns)

        for row,result in results.iterrows():
            if len(result['itemsets'])==2:
                nodes=[nodes for nodes in list(result['itemsets'])]
                row=[nodes[0],nodes[1],result['support']]
                keyword_network = pd.concat([keyword_network,pd.DataFrame([[nodes[0],nodes[1],result['support']]],columns=keyword_network.columns)])
        #각 노드의 빈도수를 이용해서 추후에 그래프의 노드 사이즈로 활용한다.
        #각 노드의 빈도수를 이용해서 추후에 그래프의 노드 사이즈로 활용한다.
        node_counts=Counter([value for values in data['target'] for value in values])
        
        return keyword_network,node_counts

    @staticmethod
    def graph_builder(network_graph, node_counts):
        plt.figure(figsize=(25,25))

        # networkx 그래프 객체를 생성합니다.
        G = nx.Graph()

        # network_graph의 키워드 빈도수를 데이터로 하여, 네트워크 그래프의 ‘노드’ 역할을 하는 원을 생성합니다. 상위 50개의 노드만 추가한다
        for node,size in node_counts.most_common(n=50):
            G.add_node(node, nodesize=size)

        # network_graph의 연관 분석 데이터를 기반으로, 네트워크 그래프의 ‘관계’ 역할을 하는 선을 생성합니다.
        for index, row in network_graph.iterrows():
            if row['source'] in G.nodes and row['target'] in G.nodes:
                G.add_weighted_edges_from([(row['source'], row['target'], row['weight'])])


        # 그래프 디자인과 관련된 파라미터를 설정합니다.
        pos = nx.spring_layout(G, k=0.6, iterations=50)
        sizes = [G.nodes[node]['nodesize']*10 for node in G]
        nx.draw(G, pos=pos, node_size=sizes)

        # print(matplotlib.rcParams)
        nx.draw_networkx_labels(G, pos=pos, font_family="Malgun Gothic", font_size=25)

        # 그래프를 출력합니다.
        ax = plt.gca()
        plt.savefig('./Results/Relation_Analyzing_Result(Twitter).png')

    @staticmethod
    def wordcloud_builder(data):

        # 도수가 높은 50개의 단어를 선정합니다.
        ranked_datas = data.most_common(50)

        # 단어의 최대 글자 크기를 80으로 제한
        data_tags = pytagcloud.make_tags(ranked_datas, maxsize=80)

        # pytagcloud 이미지를 생성합니다. 폰트는 나눔 고딕을 사용합니다.
        pytagcloud.create_tag_image(data_tags, './Results/wordcloud(Twitter).png', size=(600, 600),fontname='NanumGothic', rectangular=False)
    @staticmethod
    def analyze(data):
        network_graph,node_counts=Association_Analyzer.relation_analysis(data)
        Association_Analyzer.wordcloud_builder(node_counts)
        Association_Analyzer.graph_builder(network_graph,node_counts)

