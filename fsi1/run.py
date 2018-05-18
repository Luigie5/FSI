# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
tn = search.GPSProblem('T', 'N', search.romania)
rn = search.GPSProblem('R', 'N', search.romania)

print search.breadth_first_graph_search(ab).path()
print "Numero de nodos expandidos en la ruta AB mediante busqueda en anchura: " +str(ab.getExpandidos())+"\n"
print search.depth_first_graph_search(ab).path()
print "Numero de nodos expandidos en la ruta AB mediante busqueda en profundidad: " +str(ab.getExpandidos())+"\n"
print search.busqueda_ramificacion(ab).path()
print "Numero de nodos expandidos en la ruta AB mediante busqueda con ramificacion y acotacion: " +str(ab.getExpandidos())+"\n"
print search.busqueda_ramificacionSubestimada(ab).path()
print "Numero de nodos expandidos en la ruta AB mediante busqueda con ramificacion y acotacion con subestimacion: " +str(ab.getExpandidos())+"\n"

print search.breadth_first_graph_search(tn).path()
print "Numero de nodos expandidos en la ruta TN mediante busqueda en anchura: " +str(tn.getExpandidos())+"\n"
print search.depth_first_graph_search(tn).path()
print "Numero de nodos expandidos en la ruta TN mediante busqueda en profundidad: " +str(tn.getExpandidos())+"\n"
print search.busqueda_ramificacion(tn).path()
print "Numero de nodos expandidos en la ruta TN mediante busqueda con ramificacion y acotacion: " +str(tn.getExpandidos())+"\n"
print search.busqueda_ramificacionSubestimada(tn).path()
print "Numero de nodos expandidos en la ruta TN mediante busqueda con ramificacion y acotacion con subestimacion: " +str(tn.getExpandidos())+"\n"

print search.breadth_first_graph_search(rn).path()
print "Numero de nodos expandidos en la ruta RN mediante busqueda en anchura: " +str(rn.getExpandidos())+"\n"
print search.depth_first_graph_search(rn).path()
print "Numero de nodos expandidos en la ruta RN mediante busqueda en profundidad: " +str(rn.getExpandidos())+"\n"
print search.busqueda_ramificacion(rn).path()
print "Numero de nodos expandidos en la ruta RN mediante busqueda con ramificacion y acotacion: " +str(rn.getExpandidos())+"\n"
print search.busqueda_ramificacionSubestimada(rn).path()
print "Numero de nodos expandidos en la ruta RN mediante busqueda con ramificacion y acotacion con subestimacion: " +str(rn.getExpandidos())+"\n"

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
