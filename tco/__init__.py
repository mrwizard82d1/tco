import tco.yagl

Graph = tco.yagl.Graph

g = Graph()
g.add_edge('hou', 'mid', weight=9)
# g.add_edge('hou', 'orl', weight=4)
# g.add_edge('hou', 'okc', weight=7)
# g.add_edge('hou', 'stl', weight=11)
# g.add_edge('mid', 'hou', weight=9)
# g.add_edge('mid', 'okc', weight=6)
# g.add_edge('okc', 'stl', weight=8)
# g.add_node('van')
print('path from hou to stl == {}'.format(g.bfs('hou', 'stl')))
print('path from hou to van == {}'.format(g.bfs('hou', 'van')))

print()
g.dijkstra('hou', 'stl', 1000)
