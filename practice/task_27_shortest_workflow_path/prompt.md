# 27 — Shortest workflow path

Implement `shortest_workflow_path(graph, start, target)` for a directed, unweighted graph.

- `graph` maps each node string to a list of outgoing node strings.
- Return a list containing the shortest path from `start` to `target`, including both endpoints.
- If several shortest paths exist, return the lexicographically smallest complete path.
- Return `None` when the target is unreachable.
- `start == target` returns `[start]`.
- Reject missing nodes, duplicate neighbors, non-string/empty node names, and references to nodes absent from the graph.
- Do not mutate the graph.
- Target O(V + E) traversal time, excluding deterministic neighbor sorting.

Explain why marking nodes visited when enqueued avoids duplicate work and why BFS yields a shortest path.

Follow-up: return every shortest path without enumerating longer paths.
