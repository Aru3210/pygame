import heapq
from graphviz import Digraph

# ノードクラスの定義
class Node:
    def __init__(self, prob, symbol=None, left=None, right=None):
        self.prob = prob  # 出現確率
        self.symbol = symbol  # シンボル（文字）
        self.left = left  # 左の子ノード
        self.right = right  # 右の子ノード

    def __lt__(self, other):
        return self.prob < other.prob  # 優先度付きキュー用の比較

# ハフマン木を構築する関数
def build_huffman_tree(symbols):
    heap = [Node(prob, symbol) for symbol, prob in symbols]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.prob + right.prob, left=left, right=right)
        heapq.heappush(heap, merged)
    
    return heap[0]

# ハフマン符号を生成する関数
def generate_huffman_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node.symbol is not None:
        codebook[node.symbol] = prefix
    else:
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

# ハフマン木を描写する関数
def visualize_huffman_tree(node, graph=None, node_id=0):
    if graph is None:
        graph = Digraph(format="png")
    
    current_id = node_id
    if node.symbol is not None:  # 葉ノード
        graph.node(str(current_id), f"{node.symbol}\n{node.prob:.2f}")
    else:  # 内部ノード
        graph.node(str(current_id), f"{node.prob:.2f}")

    # 左の子ノード
    if node.left is not None:
        left_id = current_id + 1
        graph.edge(str(current_id), str(left_id), label="0")
        visualize_huffman_tree(node.left, graph, left_id)

    # 右の子ノード
    if node.right is not None:
        right_id = current_id + (2 ** (node.left.prob * 10))  # 一意のIDを生成
        graph.edge(str(current_id), str(right_id), label="1")
        visualize_huffman_tree(node.right, graph, right_id)
    
    return graph

# シンボルとその出現確率
symbols = [("s1", 0.20), ("s2", 0.15), ("s3", 0.25), ("s4", 0.05), ("s5", 0.10), ("s6", 0.25)]

# ハフマン木の構築
huffman_tree = build_huffman_tree(symbols)

# ハフマン符号の生成
huffman_codes = generate_huffman_codes(huffman_tree)

# ハフマン木の描写
huffman_graph = visualize_huffman_tree(huffman_tree)
huffman_graph.render("huffman_tree", view=True)  # ファイルに保存して表示
