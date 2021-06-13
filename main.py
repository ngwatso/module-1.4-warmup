#  Adjacency List:

class Graph:
  def __init__(self):
    self.vertices = {
      "A": { "B": 1 },
      "B": { "E": 1, "D": 2, "C": 3 },
      "C": { "E": 4 },
      "D": { "E": 2 },
      "E": { "F": 3 },
      "F": {},
      "G": { "D": 1 }
    }

#  Adjacency Matrix:

class Graph:
  def __init__(self):
    self.edges = [[0,1,0,0,0,0,0],
                  [0,0,3,2,1,0,0],
                  [0,0,0,0,4,0,0],
                  [0,0,0,0,2,0,0],
                  [0,0,0,0,0,3,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,1,0,0,0]
    ]



# ===============


class Vertex:
  def __init__(self, value):
    self.value = value
    self.connections = {}

  def __str__(self):
    return str(self.value) + ' connections: ' + str([x.value for x in self.connections])

  def add_connection(self, vert, weight = 0):
    self.connections[vert] = weight

  def get_connections(self):
    return self.connections.keys()

  def get_value(self):
    return self.value

  def get_weight(self, vert):
    return self.connections[vert]


# ===============



  class Graph:
    def __init__(self):
      self.vertices = {}
      self.count = 0

    def __contains__(self, vert):
      return vert in self.vertices

    def __iter__(self):
      return iter(self.vertices.values())

    def add_vertex(self, value):
      self.count += 1
      newVert = Vertex(value)
      self.vertices[value] = newVert
      return newVert

    def add_edge(self, v1, v2, weight = 0):
      if v1 not in self.vertices:
        self.add_vertex(v1)
      if v2 not in self.vertices:
        self.add_vertex(v2)
      self.vertices[v1].add_connection(self.vertices[v2], weight)

    def get_vertices(self):
      return self.vertices.keys()