EDGE_DIST = 6

def shortest_dist(next_node, start, end):
    if len(next_node[start]) == 0:
        return -1

    came_from = {}
    to_visit = [start]
    dist_so_far = {start: 0}

    while len(to_visit) != 0:
        current = to_visit.pop(0)

        if current == end:
            break

        for next in next_node[current]:
            new_dist = dist_so_far.get(current, 0) + EDGE_DIST

            if next not in dist_so_far or new_dist < dist_so_far[next]:
                dist_so_far[next] = new_dist
                came_from[next] = current
                to_visit.append(next)

    return dist_so_far.get(end, None) or -1

def solution(next_node, start):
    return [
        shortest_dist(next_node, start, node) for node in next_node.keys()
        if node != start
    ]

if __name__ == "__main__":
    next_node = {
        1: [2, 4, 5],
        2: [3],
        3: [4],
        4: [5, 6],
        5: [],
        6: []
    }

    start = 1

    print ' '.join([str(e) for e in solution(next_node, start)])
