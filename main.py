from src.maze import Maze
from src.draw import Draw


def main():
    row = 15
    col = 15
    draw = Draw(row, col, line_len=30)

    maze = Maze(row, col)
    min_span_tree = maze.get_min_span_tree()
    print(min_span_tree)
    draw.display_span_tree(min_span_tree)
    draw.display_self(min_span_tree)


if __name__ == "__main__":
    main()
