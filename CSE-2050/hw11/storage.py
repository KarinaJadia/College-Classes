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