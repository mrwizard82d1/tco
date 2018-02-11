import tco.yagl

Graph = tco.yagl.Graph

g = Graph()
g.add_edge('hou', 'mid', weight=9)
g.add_edge('hou', 'orl', weight=4)
g.add_edge('hou', 'okc', weight=7)
g.add_edge('hou', 'stl', weight=11)
g.add_edge('mid', 'hou', weight=9)
g.add_edge('mid', 'okc', weight=6)
g.add_edge('okc', 'stl', weight=8)
g.add_edge('stl', 'chi', weight=4)
g.add_node('van')
print('path from hou to chi == {}'.format(g.bfs('hou', 'chi')))
print('path from hou to van == {}'.format(g.bfs('hou', 'van')))

print()

def print_path_and_distance(source, target, result):
    try:
        path, dist = result
        result_text = 'path {} of distance {}'.format(path, dist)
    except TypeError:
        result_text = 'no path'
    print('Found {} from {} to {}'. format(result_text, source, target))

print_path_and_distance('hou', 'chi', g.dijkstra('hou', 'chi', 1000))
print_path_and_distance('hou', 'stm', g.dijkstra('hou', 'stm'))
print_path_and_distance('hou', 'van', g.dijkstra('hou', 'van'))
