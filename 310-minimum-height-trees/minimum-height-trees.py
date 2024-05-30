class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        edges_count = {}
        leaves = deque()
        for src, nbr in adj.items():
            if(len(nbr)) == 1:
                leaves.append(src)
            edges_count[src] = len(nbr)
        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for nbr in adj[leaf]:
                    edges_count[nbr] -= 1
                    if edges_count[nbr] == 1:
                        leaves.append(nbr)
        # return leaves