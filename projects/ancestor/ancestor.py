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
    qq = Queue()
    connections = dict()

    for connection_pairs in ancestors:
        # get the "child" key, create empty list if not in the connections dictionary
        connections[connection_pairs[1]] = connections.get(connection_pairs[1], [])
        # get the "parent" key, create empty list if not in the connections dictionary
        connections[connection_pairs[0]] = connections.get(connection_pairs[0], [])
        # connect parent to child
        connections[connection_pairs[1]].append(connection_pairs[0])

    if connections[starting_node] == [] # if the starting node has no parents

    visited = set()
    paths = list()
