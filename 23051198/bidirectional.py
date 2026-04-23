
from collections import deque
def bidirectional_bfs(graph, start, goal):
    if start == goal:
        return [start]

    q_start = deque([start])
    q_goal = deque([goal])

    visited_start = {start: None}
    visited_goal = {goal: None}

    while q_start and q_goal:
        result = expand(graph, q_start, visited_start, visited_goal)
        if result:
            return result

        result = expand(graph, q_goal, visited_goal, visited_start)
        if result:
            return result

    return None


def expand(graph, queue, visited_this, visited_other):
    current = queue.popleft()

    for neighbor in graph[current]:
        if neighbor not in visited_this:
            visited_this[neighbor] = current
            queue.append(neighbor)

            if neighbor in visited_other:
                return build_path(neighbor, visited_this, visited_other)

    return None


def build_path(meet, visited_start, visited_goal):
    path_start = []
    node = meet

    while node is not None:
        path_start.append(node)
        node = visited_start[node]

    path_goal = []
    node = visited_goal[meet]

    while node is not None:
        path_goal.append(node)
        node = visited_goal[node]

    return path_start[::-1] + path_goal

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    if start == goal:
        return path

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if result:
                return result

    return None


if __name__ == "__main__":

    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start = 'A'
    goal = 'F'

    print("Start Node:", start)
    print("Goal Node:", goal)

    print("\nBi-directional BFS Path:")
    print(bidirectional_bfs(graph, start, goal))

    print("\nStandard BFS Path:")
    print(bfs(graph, start, goal))

    print("\nDFS Path:")
    print(dfs(graph, start, goal))