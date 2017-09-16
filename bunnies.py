import copy

maxint = 999999


def dijkstra(src, dest, graph):
    graph[src]['dist'] = 0
    stack = [graph[src]]
    goal = graph[dest]

    while stack:
        stack.sort(key=lambda x: x['dist'], reverse=True)

        u = stack.pop()
        u['visited'] = True
        if u == goal:
            return goal['dist'] + 1

        for v in u['neighbours']:
            v = graph[v]
            if v['visited']:
                continue
            alt = u['dist'] + 1
            if alt < v['dist']:
                v['dist'] = alt
                v['prev'] = u
                stack.append(v)
    return maxint


def make_graph(_maze):

    ylen = len(_maze)
    xlen = len(_maze[0])
    one_positions = [None]

    for y, row in enumerate(_maze):
        for x, c in enumerate(row):
            if c == 1:
                one_positions.append((y, x))

    for r_p in one_positions:
        graph = {}
        pos = 0
        maze = copy.deepcopy(_maze)
        if r_p is not None:
            # only do this replacement if it actually punches through a path
            # otherwise we skip generating this graph
            # it needs to increase the amount of surrounding zeros to be done
            # zeros_before = 0
            # zeros_after = 0
            y, x = r_p
            # if x y is non-reachable, don't include it
            z_count = 0
            for n in [[y + 1, x],
                      [y - 1, x],
                      [y, x + 1],
                      [y, x - 1]]:
                if 0 <= n[0] < len(maze) and 0 <= n[1] < len(maze[0]) and maze[n[0]][n[1]] == 0:
                    z_count += 1
            if z_count > 0:
                maze[y][x] = 0
            else:
                continue
        grid = [range(a * xlen, a * xlen + xlen) for a in range(ylen)]
        for y, row in enumerate(maze):
            for x, c in enumerate(row):
                if c != 1:
                    # print(pos)
                    neighbours = []
                    for i in [
                        [y + 1, x],
                        [y - 1, x],
                        [y, x + 1],
                        [y, x - 1],
                    ]:
                        if 0 <= i[0] < len(maze) and 0 <= i[1] < len(maze[0]) and maze[i[0]][i[1]] == 0:
                            try:
                                neighbours.append(grid[i[0]][i[1]])
                            except IndexError:
                                pass
                    if neighbours:
                        graph[pos] = {
                            'pos': pos,
                            'dist': maxint,
                            'visited': False,
                            'prev': None,
                            'neighbours': neighbours
                        }
                pos += 1
        yield graph


def answer(maze):
    # brute force by trying all possible removals (or no removals)?
    # might take a long time
    return min(dijkstra(0, len(maze) * len(maze[0]) - 1, graph) for graph in make_graph(maze))


if __name__ == "__main__":
    # print(answer([[0, 1, 1, 0],
    #               [0, 0, 0, 1],
    #               [1, 1, 0, 0],
    #               [1, 1, 1, 0]]))
    # print(answer([[0, 0, 0, 0, 0, 0],
    #               [1, 1, 1, 1, 1, 0],
    #               [0, 0, 0, 0, 0, 0],
    #               [0, 1, 1, 1, 1, 1],
    #               [0, 1, 1, 1, 1, 1],
    #               [0, 0, 0, 0, 0, 0]]
    #              ))
    print(answer([[0, 0, 0, 0, 0, 0, 1, 1],
                  [1, 1, 1, 1, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0, 0, 1, 1],
                  [0, 1, 1, 1, 0, 1, 1, 1],
                  [0, 1, 1, 1, 0, 1, 1, 1],
                  [0, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 1, 0, 0, 0, 0, 0]]
                 ))
    print(answer([[0, 0, 0, 0, 0, 0, 1, 1],
                  [1, 1, 1, 1, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0, 0, 1, 1],
                  [0, 1, 1, 1, 0, 1, 1, 1],
                  [0, 1, 1, 1, 0, 1, 1, 1],
                  [0, 1, 1, 1, 1, 1, 1, 1],
                  [0, 1, 1, 1, 1, 1, 1, 1],
                  [0, 1, 1, 1, 1, 1, 1, 1],
                  [0, 1, 1, 1, 1, 1, 1, 1],
                  [0, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 1, 0, 0, 0, 0, 0]]
                 ))
