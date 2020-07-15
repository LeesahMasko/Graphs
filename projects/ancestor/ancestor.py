class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    # check if node is in ancestors data and pull it out of it
    found_node = None
    for node in ancestors:
        # found node as a child in a node pair
        if starting_node is node[1]:
            found_node = node
            break
    if found_node is None:
        return -1
    visited = set()
    queue = []
    queue.insert(0, found_node)
    while len(queue) > 0:
        node = queue.pop(0)
        # check if node is parent to starting node
        parent = node[0]
        if node not in visited:
            visited.add(node)
            # find a parent pointing to this node
            for ancestor in ancestors:
                # a parent node pointing to another parent
                if ancestor[1] is parent:
                    # queue that to check again
                    queue.append(ancestor)
                    break
    return parent
    # qq = Queue()
    # connections = dict()

    # for connection_pairs in ancestors:
    #     # get the "child" key, create empty list if not in the connections dictionary
    #     connections[connection_pairs[1]] = connections.get(connection_pairs[1], [])
    #     # get the "parent" key, create empty list if not in the connections dictionary
    #     connections[connection_pairs[0]] = connections.get(connection_pairs[0], [])
    #     # connect parent to child
    #     connections[connection_pairs[1]].append(connection_pairs[0])

    # if connections[starting_node] == [] # if the starting node has no parents

    # visited = set()
    # paths = list()



    ###  loop through, add nodes to visited once visited
    ###  search paths
    ###  find the longest path
    ###  Check to see if there are any paths that are the same length as the longest path
    ###  find the last index (maybe sort to put the last index first???)
