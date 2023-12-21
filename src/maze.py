import random


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # For directions of cells
        self.TOP = 0
        self.BOTTOM = 1
        self.LEFT = 2
        self.RIGHT = 3

        self.frontier_cells = []

    def get_adjacencies(self, idx):
        # Top, bottom, left, right
        top, bottom, left, right = None, None, None, None
        if idx > self.width:
            top = idx - self.width
        if (idx + self.width) < (self.width * self.height - 1):
            bottom = idx + self.width
        if (idx + 1) % self.width != 0:
            right = idx + 1
        if idx % self.width != 0:
            left = idx
        return [top, bottom, left, right]

    def get_edges(self, visited):
        edges = []
        for idx in visited:
            top, bottom, left, right = self.get_adjacencies(idx)

            if top is not None and top not in visited:
                edges.append((idx, self.TOP, top, self.BOTTOM))
            if bottom is not None and bottom not in visited:
                edges.append((idx, self.BOTTOM, bottom, self.TOP))
            if left is not None and left not in visited:
                edges.append((idx, self.LEFT, left, self.RIGHT))
            if right is not None and right not in visited:
                edges.append((idx, self.RIGHT, right, self.LEFT))
        return edges

    def get_min_span_tree(self):
        min_span_tree = [[0, 0, 0, 0] for _ in range(self.width * self.height)]
        to_visit = [cell for cell in range(len(min_span_tree))]

        # Random row and col that aren't on the edge
        starting_idx = 0
        visited = [starting_idx]
        to_visit.remove(starting_idx)

        i = 0
        while len(to_visit) > 0:
            i += 1
            if i % 10 == 0:
                print(f"{i} iterations")

            edges = self.get_edges(visited)

            if len(edges) == 0:
                print("No edges found")
                break

            from_cell, from_direction, to_cell, to_direction = random.choice(edges)

            min_span_tree[to_cell][to_direction] = 1
            min_span_tree[from_cell][from_direction] = 1

            visited.append(to_cell)
            to_visit.remove(to_cell)

        return min_span_tree
