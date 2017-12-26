import math
from queue import PriorityQueue


def shortest_path(M, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    explored = {start: None}
    gscore = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            reconstruct_path(explored, start, goal)

        for next in M.roads[current]:
            tentative_gscore = gscore[current] + heuristic(M, current, next)
            if next not in gscore or tentative_gscore < gscore[next]:
                gscore[next] = tentative_gscore
                fscore = tentative_gscore + heuristic(M, goal, next)
                frontier.put(next, fscore)
                explored[next] = current

    return reconstruct_path(explored, start, goal)


def reconstruct_path(explored, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = explored[current]
        path.append(current)
    path.reverse()
    return path


def heuristic(M, n1, n2):
    a = M.intersections[n1]
    b = M.intersections[n2]
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)