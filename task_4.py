import uuid

import matplotlib.pyplot as plt
import networkx as nx

from min_heap import MinHeap


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
    if node.left:
        graph.add_edge(node.id, node.left.id)
        l = x - 1 / 2**layer
        pos[node.left.id] = (l, y - 1)
        add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
        graph.add_edge(node.id, node.right.id)
        r = x + 1 / 2**layer
        pos[node.right.id] = (r, y - 1)
        add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Бінарне дерево"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    fig, ax = plt.subplots(figsize=(10, 6))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
        font_size=10,
        font_weight="bold",
        ax=ax,
    )
    ax.set_title(title)
    if fig.canvas.manager is not None:
        fig.canvas.manager.set_window_title(title)
    fig.tight_layout()
    plt.show()


def heap_to_tree(heap):
    if not heap:
        return None

    nodes = [Node(value) for value in heap]

    for i in range(len(heap)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(heap):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(heap):
            nodes[i].right = nodes[right_idx]

    nodes[0].color = "lightgreen"
    return nodes[0]


def visualize_heap(heap, title="Бінарна купа (мін-купа)"):
    root = heap_to_tree(heap)
    if root is None:
        print("Купа порожня.")
        return
    draw_tree(root, title=title)


def build_min_heap(values):
    heap = MinHeap()
    for value in values:
        heap.push(value)
    return heap.heap


if __name__ == "__main__":
    # Приклад звичайного бінарного дерева (базовий код)
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    draw_tree(root, title="Приклад бінарного дерева")

    # Візуалізація бінарної купи як дерева
    heap_array = build_min_heap([20, 15, 10, 8, 12, 5, 3, 2, 7])
    print("Масив купи:", heap_array)
    visualize_heap(heap_array)
