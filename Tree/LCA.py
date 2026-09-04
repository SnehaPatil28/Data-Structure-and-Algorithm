def lca(u, v, depth, parent):
    """
    Finds the Lowest Common Ancestor (LCA) of two nodes using binary lifting.

    Args:
        u: The first node.
        v: The second node.
        depth: A list containing the depth of each node.
        parent: A 2D list where parent[i][node] is the 2**i-th ancestor of node.

    Returns:
        The LCA of u and v.
    """
    # Ensure u is deeper than v
    if depth[u] < depth[v]:
        u, v = v, u

    # Lift u to the same depth as v
    diff = depth[u] - depth[v]
    i = 0
    while diff:
        if diff & 1:  # Check if the i-th bit is set
            u = parent[i][u]
        diff >>= 1  # Right-shift to check the next bit
        i += 1

    # If v is the ancestor of u, then v is the LCA
    if u == v:
        return u

    # Lift both u and v until their parents are the same
    for i in reversed(range(len(parent))):
        if parent[i][u] != parent[i][v]:
            u = parent[i][u]
            v = parent[i][v]

    # The parent of u is the LCA
    return parent[0][u]
