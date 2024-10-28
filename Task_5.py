import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree, pos, node_colors):
    plt.clf()
    nx.draw(tree, pos=pos, labels={node: tree.nodes[node]['label'] for node in tree.nodes},
             node_color=node_colors, node_size=2500, font_color="white", font_size=10, arrows=False)
    plt.pause(0.5)


def generate_colors(num_nodes):
    """Генерує кольори від темного до світлого."""
    return ["#" + ''.join(f"{int(c * 255):02x}" for c in colorsys.hsv_to_rgb(0.6, i / num_nodes, 1)) for i in range(num_nodes)]


def dfs(tree, root):
    stack = [root]
    visited = set()
    colors = generate_colors(tree.number_of_nodes())
    pos = {root.id: (0, 0)}
    graph = add_edges(nx.DiGraph(), root, pos)
    node_colors = ["#a0a0a0" for _ in range(graph.number_of_nodes())]  # Початковий колір вузлів

    i = 0
    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            node_colors[list(graph.nodes).index(node.id)] = colors[i]
            i += 1
            draw_tree(graph, pos, node_colors)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def bfs(tree, root):
    queue = [root]
    visited = set()
    colors = generate_colors(tree.number_of_nodes())
    pos = {root.id: (0, 0)}
    graph = add_edges(nx.DiGraph(), root, pos)
    node_colors = ["#a0a0a0" for _ in range(graph.number_of_nodes())]  # Початковий колір вузлів

    i = 0
    while queue:
        node = queue.pop(0)
        if node.id not in visited:
            visited.add(node.id)
            node_colors[list(graph.nodes).index(node.id)] = colors[i]
            i += 1
            draw_tree(graph, pos, node_colors)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# Створення дерева
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

# Візуалізація обходів
print("DFS обход дерева:")
dfs(root, root)
plt.pause(2)  # Пауза перед переходом до BFS
print("BFS обход дерева:")
bfs(root, root)
plt.show()
