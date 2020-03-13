from apyori import apriori
from konlpy.tag import Okt
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

class Relation_Analyzer:
    @staticmethod
    def relation_analysis(data):
        #키워드 간에 연관성 분석을 진행한다.
        transactions=data['target'].tolist()
        transactions = [transaction for transaction in transactions if transaction]
        results = list(apriori(transactions,
                               min_support=0.1,
                               min_confidence=0.2,
                               min_lift=5,
                               max_length=2))

        #노드 2개가 서로 연결되어 있는 구조를 추출한다.
        columns=['source','target','weight']
        keyword_network=pd.DataFrame(columns=columns)

        for result in results:
            if len(result)==2:
                nodes=[nodes for nodes in result.items]
                row=[nodes[0],nodes[1],result.support]
                keyword_network.append(pd.Series(row,index=keyword_network.columns),ignore_index=True)

        #각 노드의 빈도수를 이용해서 추후에 그래프의 노드 사이즈로 활용한다.
        nouns_extract=Okt()
        nouns=nouns_extract.nouns("".join(data['ko-text']))
        noun_counts=Counter(nouns)
        noun_counts=Counter({noun : noun_counts[noun] for noun in noun_counts if len(noun) >1})

        return keyword_network,noun_counts

    @staticmethod
    def graph_builder(network_graph, node_counts):
        plt.figure(figsize=(25,25))

        # networkx 그래프 객체를 생성합니다.
        G = nx.Graph()

        # network_graph의 키워드 빈도수를 데이터로 하여, 네트워크 그래프의 ‘노드’ 역할을 하는 원을 생성합니다.
        for index, row in network_graph.iterrows():
            G.add_node(row['node'], nodesize=row['nodesize'])

        # network_graph의 연관 분석 데이터를 기반으로, 네트워크 그래프의 ‘관계’ 역할을 하는 선을 생성합니다.
        for index, row in network_graph.iterrows():
            G.add_weighted_edges_from([(row['source'], row['target'], row['weight'])])

        # 그래프 디자인과 관련된 파라미터를 설정합니다.
        pos = nx.spring_layout(G, k=0.6, iterations=50)
        sizes = [G.node[node]['nodesize']*25 for node in G]
        nx.draw(G, pos=pos, node_size=sizes)

        # Windows 사용자는 AppleGothic 대신,'Malgun Gothic'. 그 외 OS는 OS에서 한글을 지원하는 기본 폰트를 입력합니다.
        nx.draw_networkx_labels(G, pos=pos, font_family='AppleGothic', font_size=25)

        # 그래프를 출력합니다.
        ax = plt.gca()
        plt.savefig('./Relation_Analyzing_Result.png')

    @staticmethod
    def analyze(data):
        network_graph,node_counts=Relation_Analyzer.relation_analysis(data)
        print(network_graph,node_counts)
        Relation_Analyzer.graph_builder(network_graph,node_counts)

