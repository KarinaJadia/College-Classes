class Graph:
    def __init__(self, V=(), E=()):
        """ initializes a non-directional, edge-weighted graph with a set of vertices and edges """
        self.adj = {}
        for v in V:
            self.add_vertex(v)
        for u, v, wt in E:
            self.add_edge(u, v, wt)


    def add_vertex(self, v):
        """ adds a vertex to the graph, for add_edge """
        if v not in self.adj:
            self.adj[v] = {}


    def remove_vertex(self, v):
        """ removes a vertex from the graph """
        if v in self.adj:
            for u in self.adj[v]:
                del self.adj[u][v]
            del self.adj[v]


    def add_edge(self, u, v, wt):
        """ adds an edge to the graph between vertices u and v with weight wt """
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u][v] = wt
        self.adj[v][u] = wt


    def remove_edge(self, u, v, wt):
        """ removes an edge from the graph between vertices u and v with weight wt """
        if u in self.adj and v in self.adj[u] and self.adj[u][v] == wt:
            del self.adj[u][v]
            del self.adj[v][u]


    def has_edge(self, u, v):
        """ returns if edge in graph, made for unittests """
        return u in self.adj and v in self.adj[u]


    def nbrs(self, v):
        """ returns an iterator over the neighbors of vertex v """
        if v in self.adj:
            for neighbor in self.adj[v]:
                yield neighbor
                

    def bfs(self, src):
        """ breadth-first search algorithm to find the shortest path between a source vertex and all other vertices in the graph """
        # initializes visited set, queue, previous vertex dictionary, and distance dictionary
        visited = {src}
        queue = [(src, 0)]
        prev = {src: None}
        dist = {src: 0}
        
        # performs BFS traversal
        while queue:
            # dequeues vertex and its distance from source
            u, d = queue.pop(0)
            # explores neighbors of dequeued vertex
            for v in self.nbrs(u):
                if v not in visited:
                    # marks neighbor as visited, enqueue it, and update previous and distance dictionaries
                    visited.add(v)
                    queue.append((v, d+1))
                    prev[v] = u
                    dist[v] = d+1
        
        # returns previous and distance dictionaries
        return prev, dist


    def fewest_flights(self, city):
            """ finds how to get from city to any other city in the graph with the fewest number of flights """
            prev, dist = self.bfs(city)
            return prev, dist


    def shortest_path(self, city):
        """ I used Dijkstra's algorithm to find the shortest path between a source vertex and all other vertices in the graph """
        # initializes priority queue, visited set, and dictionaries for prev and dist
        pq = [(0, city)]
        visited = set()
        prev = {}
        dist = {city: 0}

        # loops until priority queue is empty
        while pq:
            # extracts the vertex with the smallest distance from the priority queue
            pq.sort()
            d, u = pq.pop(0)
            # skips vertices that have already been visited
            if u in visited:
                continue
            # adds vertex u to visited set and update its distance
            visited.add(u)
            # loops over all neighbors v of u
            for v in self.nbrs(u):
                # gets the weight of the edge between u and v
                wt = self.adj[u][v]
                # if v has not been visited, updates its distance and add it to the priority queue
                if v not in visited:
                    new_d = d + wt
                    if v not in dist or new_d < dist[v]:
                        dist[v] = new_d
                        prev[v] = u
                        pq.append((new_d, v))
        
        # returns dictionaries for prev and dist
        return prev, dist


    def minimum_salt(self, city):
        """ creates a minimum salt spanning tree with city as the root vertex """
        # initalizes the set of visited vertices, the previous vertex dict, the distance dict, and the queue
        visited = {city}  # set of visited vertices, starts with the root city
        prev = {city: None}  # dictionary of previous vertices for each visited vertex
        dist = {city: 0}  # dictionary of distances from the root city to each visited vertex
        queue = [(city, 0)]  # priority queue with the root city and a distance of 0

        # while there are vertices in the queue to process
        while queue:
            # pops the vertex with the smallest distance from the priority queue
            u, d = queue.pop(0)
            
            # goes through what hasn't been visit
            for v in self.nbrs(u):
                if v not in visited:
                    # marks the neighboring vertex as visited
                    visited.add(v)
                    # adds the neighboring vertex to the queue with a new distance
                    queue.append((v, d + self.adj[u][v]))
                    # sets the previous vertex and distance for the neighboring vertex
                    prev[v] = u
                    dist[v] = self.adj[u][v]

        # returns the previous vertex dict and distance dict
        return prev, dist