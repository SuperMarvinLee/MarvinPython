class EdgeStep:
    def __init__(self,direction="BOTH",labels=[],properties={},degree=10000,skipDegree=100000):
        self.direction = direction
        self.labels = labels
        self.properties = properties
        self.max_degree = degree
        self.skip_degree = skipDegree


