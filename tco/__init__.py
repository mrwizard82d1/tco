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
path = g.bfs('hou', 'van')
print('path == {}'.format(path))
