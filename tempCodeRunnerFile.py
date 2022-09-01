    def dfs(self,vertex):
        visited =[vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)
    