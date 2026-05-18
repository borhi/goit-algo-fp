from min_heap import MinHeap


def print_table(distances, visited):
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    for vertex in distances:
        distance = distances[vertex]
        if distance == float("inf"):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print()


def build_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    if path[0] != start:
        return None
    return path


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distances[start] = 0

    heap = MinHeap()
    heap.push((0, start))
    visited = set()

    while not heap.is_empty():
        current_dist, current_vertex = heap.pop()

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current_vertex
                heap.push((new_dist, neighbor))

        print_table(distances, visited)

    return distances, previous


if __name__ == "__main__":
    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"A": 5, "D": 3},
        "C": {"A": 10, "D": 2},
        "D": {"B": 3, "C": 2, "E": 4},
        "E": {"D": 4},
    }

    start_vertex = "A"
    print(f"Алгоритм Дейкстри від вершини {start_vertex}:\n")
    distances, previous = dijkstra(graph, start_vertex)

    print("Найкоротші відстані:")
    for vertex, dist in distances.items():
        if dist == float("inf"):
            print(f"  {start_vertex} -> {vertex}: недосяжна")
        else:
            path = build_path(previous, start_vertex, vertex)
            print(f"  {start_vertex} -> {vertex}: {dist} (шлях: {' -> '.join(path)})")
