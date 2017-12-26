import math
from queue import PriorityQueue


def shortest_path(M, start, goal):
    queue = PriorityQueue()
    queue.put(start, 0)
    visited = {start: None}
    gscore = {start: 0}

    while not queue.empty():
        current = queue.get()

        if current == goal:
            reconstruct_path(visited, start, goal)

        for next in M.roads[current]:
            fscore = gscore[current] + heuristic(M, current, next)
            if next not in gscore or fscore < gscore[next]:
                gscore[next] = fscore
                priority = fscore + heuristic(M, goal, next)
                queue.put(next, priority)
                visited[next] = current

    return reconstruct_path(visited, start, goal)


def reconstruct_path(visited, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = visited[current]
        path.append(current)
    path.reverse()
    return path


def heuristic(M, n1, n2):
    a = M.intersections[n1]
    b = M.intersections[n2]
    return abs(b[0] - a[0]) + abs(b[1] - a[1])