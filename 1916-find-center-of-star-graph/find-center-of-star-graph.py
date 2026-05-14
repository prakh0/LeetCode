class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        node_count = {}
        for u,v in edges:
            if u in node_count:
                node_count[u] += 1
            else:
                node_count[u] = 1
            if v in node_count:
                node_count[v] += 1
            else:
                node_count[v] = 1
        for node in node_count:
            if node_count[node] == len(edges):
                return node