import random
from math import factorial
from string import ascii_lowercase

class Node:
    def __init__(self, name: str):
        self.name = name
        self.paths: list[Path] = []
    
    def __repr__(self):
        return f'Node(name={self.name})'


class Path:
    def __init__(self, nodes: set[Node], length: int):
        self.nodes = nodes
        self.length = length


def random_network(n_nodes: int, n_paths: int) -> None:
    assert n_nodes > 1, \
        'Needs at least 2 nodes.'
    assert n_nodes <= len(ascii_lowercase), \
        f'Maximum {len(ascii_lowercase)} possible.'
    assert n_paths >= n_nodes - 1, \
        f'Minimum {n_nodes} required.'
    assert n_paths <= factorial(n_nodes - 1), \
        f'Maximum {min(factorial(n_nodes - 1), n_nodes)} possible.'
    
    nodes: list[Node] = []
    for char in ascii_lowercase:
        nodes.append(Node(char))
        if len(nodes) == n_nodes:
            break
    
    unlinked_nodes = nodes.copy()
    random.shuffle(unlinked_nodes)
    node = unlinked_nodes.pop()
    paths = 0
    while unlinked_nodes:
        companion = unlinked_nodes.pop()
        path = Path({node, companion})
        paths += 1
        node.paths.append(path)
        companion.paths.append(path)
        node = companion
    
    while paths < n_paths:
        node = random.choice(nodes)
        companion = random.choice(nodes)
        if node == companion:
            continue
        if {node, companion} in [path.nodes for path in node.paths]:
            continue
        path = Path({node, companion})
        paths += 1
        node.paths.append(path)
        companion.paths.append(path)
    
    return nodes

def ucs(start: Node, end: Node) -> tuple[int, list[Node]]|None:
    queue: list[tuple[int, list[Node]]] = [(0, [start])]
    expanded: set[Node] = set()

    while queue:
        queue.sort(key=lambda x: x[0], reverse=True)
        node_info = queue.pop()
        node = node_info[1][-1]

        if node == end:
            return node_info
        
        if node in expanded:
            continue

        expanded.add(node)

        for path in node.paths:
            [neighbour] = path.nodes.difference({node})
            
            if neighbour in expanded:
                continue

            new_length = node_info[0] + path.length
            new_route = node_info[1].copy()
            new_route.append(neighbour)
            queue.append((new_length, new_route))
    
    return None

if __name__ == '__main__':
    nodes = {
        'S': Node('S'),
        '1': Node('1'),
        '2': Node('2'),
        '3': Node('3'),
        '4': Node('4'),
        '5': Node('5'),
        'G': Node('G'),
    }

    paths = {
        'S1': Path({nodes['S'], nodes['1']}, 2),
        'S3': Path({nodes['S'], nodes['3']}, 5),
        '13': Path({nodes['1'], nodes['3']}, 5),
        '1G': Path({nodes['1'], nodes['G']}, 1),
        '12': Path({nodes['1'], nodes['2']}, 4),
        '24': Path({nodes['2'], nodes['4']}, 4),
        '25': Path({nodes['2'], nodes['5']}, 6),
        '3G': Path({nodes['3'], nodes['G']}, 6),
        '34': Path({nodes['3'], nodes['4']}, 2),
        '45': Path({nodes['4'], nodes['5']}, 3),
        '4G': Path({nodes['4'], nodes['G']}, 7),
        '5G': Path({nodes['5'], nodes['G']}, 3),
    }

    for node_names, path in paths.items():
        node_1, node_2 = list(node_names)
        nodes[node_1].paths.append(path)
        nodes[node_2].paths.append(path)
    
    start = 'S'
    end = 'G'
    shortest_path = ucs(nodes[start], nodes[end])
    if shortest_path:
        print(f'Shortest path from {start} to {end} is {shortest_path[0]}')
    else:
        print(f'No path found from {start} to {end}')
    