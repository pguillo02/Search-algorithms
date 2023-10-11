# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("Búsqueda con ramificación y acotación")
bb = search.branch_and_bound(ab).path()
print(bb)

print("<---------------------------------------------------------------------------------->")

print("Búsqueda con ramificación y acotación con subestimación")
bs = search.branch_and_bound_sub(ab).path()
print(bs)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
