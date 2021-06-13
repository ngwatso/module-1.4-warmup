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