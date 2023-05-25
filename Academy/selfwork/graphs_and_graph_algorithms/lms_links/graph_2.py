# Create the dictionary with graph elements
graph = {
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
# Print the graph
print(graph)

class Graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = []
      self.gdict = gdict

# Get the keys of the dictionary
   def get_vertices(self):
      return list(self.gdict.keys())

   def edges(self):
      return self.find_edges()

# Find the distinct list of edges
   def find_edges(self):
      edge_name = []
      for vrtx in self.gdict:
         for nxtvrtx in self.gdict[vrtx]:
            if {nxtvrtx, vrtx} not in edge_name:
               edge_name.append({vrtx, nxtvrtx})
      return edge_name

# Add the vertex as a key
   def add_vertex(self, vrtx):
      if vrtx not in self.gdict:
         self.gdict[vrtx] = []

# Add the new edge
   def add_edge(self, edge):
      edge = set(edge)
      (vrtx1, vrtx2) = tuple(edge)
      if vrtx1 in self.gdict:
         self.gdict[vrtx1].append(vrtx2)
      else:
         self.gdict[vrtx1] = [vrtx2]


if __name__ == "__main__":

    # Create the dictionary with graph elements
    graph_elements = {
       "a" : ["b","c"],
       "b" : ["a", "d"],
       "c" : ["a", "d"],
       "d" : ["e"],
       "e" : ["d"]
    }
    g = Graph(graph_elements)
    print(g.get_vertices())
    print(g.edges())
    g.add_vertex("f")
    print(g.get_vertices())
    g.add_edge({'a', 'e'})
    g.add_edge({'a', 'c'})
    print(g.edges())
