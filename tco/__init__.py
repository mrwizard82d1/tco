import tco.yagl

Graph = tco.yagl.Graph

g = Graph()
g.add_edge('hou', 'mid')
g.add_edge('hou', 'okc')
g.add_edge('hou', 'orl')
g.add_edge('mid', 'hou')
g.add_edge('mid', 'okc')
g.add_edge('okc', 'stl')
g.add_node('van')
print('path from hou to stl == {}'.format(g.bfs('hou', 'stl')))
print('path from hou to van == {}'.format(g.bfs('hou', 'van')))
