import heapq
from node import Node

class AStar:
    # Initialize the A* algorithm with given nodes, start node, end node, and barrier nodes
    def __init__(self, nodes, start_node, end_node, barrier_nodes):
        self.nodes = nodes
        self.start_node = start_node
        self.end_node = end_node
        self.barrier_nodes = barrier_nodes
        # Create an open set and add the start node with a score of 0
        self.open_set = []
        heapq.heappush(self.open_set, (0, self.start_node))
        # Create dictionaries to store the path and scores for each node
        self.came_from = {}
        self.g_scores = {node: float('inf') for row in nodes for node in row}
        self.g_scores[start_node] = 0
        self.f_scores = {node: float('inf') for row in nodes for node in row}
        self.f_scores[start_node] = self.heuristic(start_node, end_node)
        # Create a set to store nodes that are in the open set
        self.open_set_hash = {self.start_node}
        # Initialize finished to False
        self.finished = False
 
    def step(self):
        # Take a step in the A* algorithm
        if not self.open_set:
            # If the open set is empty, the algorithm is finished
            self.finished = True
            return
        # Get the node with the lowest f-score from the open set
        current_node = heapq.heappop(self.open_set)[1]
        # Remove the current node from the open set hash
        self.open_set_hash.remove(current_node)
        # If the current node is the end node, the algorithm is finished
        if current_node == self.end_node:
            self.finished = True
            return
        # Check the neighbors of the current node
        for neighbor in self.get_neighbors(current_node):
            # Calculate the tentative g-score for the neighbor
            tentative_g_score = self.g_scores[current_node] + self.distance(current_node, neighbor)
            # If the tentative g-score is lower than the current g-score for the neighbor, update the scores
            if tentative_g_score < self.g_scores[neighbor]:
                self.came_from[neighbor] = current_node
                self.g_scores[neighbor] = tentative_g_score
                self.f_scores[neighbor] = tentative_g_score + self.heuristic(neighbor, self.end_node)
                # If the neighbor is not in the open set hash, add it to the open set with its f-score
                if neighbor not in self.open_set_hash:
                    heapq.heappush(self.open_set, (self.f_scores[neighbor], neighbor))
                    self.open_set_hash.add(neighbor)
                    if neighbor != self.end_node:
                        neighbor.color = Node.OPEN_COLOR
                if current_node != self.start_node:
                    current_node.color = Node.CLOSED_COLOR
                
    def reconstruct_path(self):
        # Reconstruct the path from the start node to the end node using the came_from dictionary
        path = []
        node = self.end_node
        while node in self.came_from:
            path.insert(0, node)
            node = self.came_from[node]
        path.insert(0, self.start_node)
        return path

    def get_neighbors(self, node):
        # Get the neighbors of a given node that are not barriers
        neighbors = []
        if node.row > 0:
            top_node = self.nodes[node.row - 1][node.col]
            if top_node not in self.barrier_nodes:
                neighbors.append(top_node)
        if node.row < len(self.nodes) - 1:
            bottom_node = self.nodes[node.row + 1][node.col]
            if bottom_node not in self.barrier_nodes:
                neighbors.append(bottom_node)
        if node.col > 0:
            left_node = self.nodes[node.row][node.col - 1]
            if left_node not in self.barrier_nodes:
                neighbors.append(left_node)
        if node.col < len(self.nodes[0]) - 1:
            right_node = self.nodes[node.row][node.col + 1]
            if right_node not in self.barrier_nodes:
                neighbors.append(right_node)
        return neighbors

    def heuristic(self, node1, node2):
        # Calculates the heuristic score (Manhattan distance) between two nodes
        return abs(node1.row - node2.row) + abs(node1.col - node2.col)

    def distance(self, node1, node2):
        # Calculates the distance (1 or sqrt(2)) between two adjacent nodes
        return 1 if node1.row == node2.row or node1.col == node2.col else 1.4
