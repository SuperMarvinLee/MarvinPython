class KoutRequest:
    def __init__(self,source,step,maxDepth=10000,nearest=True,capacity=10000000,limit=10,withVertex=False,withPath=False):
        self.source = source
        self.step = step
        self.max_depth = maxDepth
        self.nearest = nearest
        self.capacity = capacity
        self.limit = limit
        self.with_vertex = withVertex
        self.with_path = withPath
