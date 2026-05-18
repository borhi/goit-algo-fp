from collections import deque

import matplotlib.pyplot as plt
import networkx as nx

from task_4 import Node, add_edges

BASE_RGB = (0x12, 0x96, 0xF0)
DEFAULT_COLOR = "#D3D3D3"
STEP_PAUSE = 1.5


def color_for_step(step, total):
    if total <= 1:
        ratio = 1.0
    else:
        ratio = step / (total - 1)

    dark = tuple(int(channel * 0.2) for channel in BASE_RGB)
    light = tuple(int(channel + (255 - channel) * 0.9) for channel in BASE_RGB)

    r = int(dark[0] + (light[0] - dark[0]) * ratio)
    g = int(dark[1] + (light[1] - dark[1]) * ratio)
    b = int(dark[2] + (light[2] - dark[2]) * ratio)
    return f"#{r:02X}{g:02X}{b:02X}"


def collect_nodes(root):
    if root is None:
        return []

    nodes = []
    stack = [root]
    while stack:
        node = stack.pop()
        nodes.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return nodes


def dfs_order(root):
    if root is None:
        return []

    order = []
    stack = [root]

    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order


def bfs_order(root):
    if root is None:
        return []

    order = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return order


def draw_tree_state(root, title):
    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(graph, root, pos)

    colors = [data["color"] for _, data in graph.nodes(data=True)]
    labels = {node_id: data["label"] for node_id, data in graph.nodes(data=True)}

    fig, ax = plt.subplots(figsize=(10, 6))
    nx.draw(
        graph,
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
    return fig


def reset_colors(root):
    for node in collect_nodes(root):
        node.color = DEFAULT_COLOR


def visualize_traversal(root, order, traversal_name):
    total = len(order)
    reset_colors(root)

    for step, node in enumerate(order):
        node.color = color_for_step(step, total)
        visited = [n.val for n in order[: step + 1]]
        title = (
            f"{traversal_name} — крок {step + 1}/{total}: "
            f"відвідано {node.val} | порядок: {visited}"
        )
        fig = draw_tree_state(root, title)
        plt.show(block=False)
        plt.pause(STEP_PAUSE)
        plt.close(fig)


def build_sample_tree():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root


if __name__ == "__main__":
    tree_root = build_sample_tree()

    dfs_nodes = dfs_order(tree_root)
    print("DFS (стек):", [node.val for node in dfs_nodes])
    visualize_traversal(tree_root, dfs_nodes, "Обхід у глибину (DFS)")

    bfs_nodes = bfs_order(tree_root)
    print("BFS (черга):", [node.val for node in bfs_nodes])
    visualize_traversal(tree_root, bfs_nodes, "Обхід у ширину (BFS)")
