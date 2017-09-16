# generate: the complete graph from the chessboard,
# ie. for each position, set neighbours to all the possible
# L shaped moves,
# solve by using dijkstra to get from src to dst

"""
-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------
"""

maxint = 99999


def gen_graph():
    # graph is just a dict from {x -> [p1,p2..pn    ]}
    # generate a chessboard
    graph = {}
    board = [range(a * 8, a * 8 + 8) for a in range(8)]
    for y, row in enumerate(board):
        for x, c in enumerate(row):
            neighbours = []

            for i in [
                [x + 2, y + 1],
                [x + 2, y - 1],
                [x - 2, y + 1],
                [x - 2, y - 1],
                [x + 1, y + 2],
                [x + 1, y - 2],
                [x - 1, y + 2],
                [x - 1, y - 2],
            ]:
                if i[0] < 0 or i[1] < 0:
                    continue
                try:
                    neighbours.append(board[i[1]][i[0]])
                except IndexError:
                    pass
            graph[c] = {
                'pos': c,
                'dist': maxint,
                'visited': False,
                'prev': None,
                'neighbours': neighbours
            }
    return graph


def dijkstra(src, dest, graph):
    graph[src]['dist'] = 0
    stack = [graph[src]]
    goal = graph[dest]

    while stack:
        stack.sort(key=lambda x: x['dist'], reverse=True)

        u = stack.pop()
        u['visited'] = True
        if u == goal:
            return goal['dist']

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


def answer(src, dest):
    # your code here
    graph = gen_graph()
    return dijkstra(src, dest, graph)


if __name__ == "__main__":
    print(answer(19, 36))
    print(answer(0, 1))
