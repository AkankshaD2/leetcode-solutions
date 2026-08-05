class Solution(object):
    def remainingMethods(self, n, k, invocations):
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        suspicious = set()

        def dfs(node):
            if node in suspicious:
                return
            suspicious.add(node)
            for nei in graph[node]:
                dfs(nei)

        dfs(k)

        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        return [i for i in range(n) if i not in suspicious]