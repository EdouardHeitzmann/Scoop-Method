#needs cut_edges to be added to updaters
def pencil_dist(partition1,partition2):
    return len(partition1.cut_edges.difference(partition2.cut_edges))+len(partition2.cut_edges.difference(partition1.cut_edges))