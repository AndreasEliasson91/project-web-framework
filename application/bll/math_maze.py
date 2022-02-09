import itertools
import random as r

DIRECTIONS = [
    ('north', [0, -1]),
    ('south', [0, 1]),
    ('east', [1, 0]),
    ('west', [-1, 0])
]


def move(direction, x, y):
    match direction:
        case 'north':
            y -= 1
        case 'south':
            y += 1
        case 'west':
            x -= 1
        case 'east':
            x += 1

    return x, y


def difficulty_settings(difficulty):
    numbers, max_range, negative, decimals = None, None, None, None

    match difficulty:
        case 1:
            numbers = [2]
            max_range = 5
            negative = False
            decimals = False
        case 2:
            numbers = [2, 3]
            max_range = 10
            negative = False
            decimals = False
        case 3:
            numbers = [3]
            max_range = 12
            negative = False
            decimals = False
        case 4:
            numbers = [3, 4]
            max_range = 15
            negative = True
            decimals = False
        case 5:
            numbers = [4]
            max_range = 17
            negative = True
            decimals = False
        case 6:
            numbers = [4, 5]
            max_range = 20
            negative = True
            decimals = True
        case 7:
            numbers = [5]
            max_range = 30
            negative = True
            decimals = True

    return {
        'numbers': numbers,
        'max_range': max_range,
        'negative': negative,
        'decimals': decimals
    }


def write_map(maze, out_file: str):
    """
    Write a map as an SVG (Scalable Vector Graphics) image of the map
    :param maze: Maze instance, the maze to write to SVG
    :param out_file: str, the file name for the output file
    :return None
    """

    def write_wall(wall_f, wall_x1, wall_y1, wall_x2, wall_y2):
        print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'
              .format(wall_x1, wall_y1, wall_x2, wall_y2), file=wall_f)

    aspect_ratio = maze.num_of_cells_x / maze.num_of_cells_y
    padding = 10
    height = 500
    width = int(height * aspect_ratio)  # Height and width of the map image in pixels
    scale_y, scale_x = height / maze.num_of_cells_y, width / maze.num_of_cells_x  # Scaling the map coordinates

    with open(out_file, 'w') as f:
        # SVG preamble and styles.
        print('<?xml version="1.0" encoding="utf-8"?>', file=f)
        print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
        print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
        print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'
              .format(width + 2 * padding, height + 2 * padding,
                      -padding, -padding, width + 2 * padding, height + 2 * padding),
              file=f)
        print('<defs>\n<style type="text/css"><![CDATA[', file=f)
        print('line {', file=f)
        print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
        print('    stroke-width: 5;\n}', file=f)
        print(']]></style>\n</defs>', file=f)
        # Draw the "South" and "East" walls of each cell,
        # these are the "North" and "West" walls of the neighbouring cell
        for x in range(maze.num_of_cells_x):
            for y in range(maze.num_of_cells_y):
                if maze.get_cell(x, y).walls['south']:
                    x1, y1, x2, y2 = x * scale_x, (y + 1) * scale_y, (x + 1) * scale_x, (y + 1) * scale_y
                    write_wall(f, x1, y1, x2, y2)
                if maze.get_cell(x, y).walls['east']:
                    x1, y1, x2, y2 = (x + 1) * scale_x, y * scale_y, (x + 1) * scale_x, (y + 1) * scale_y
                    write_wall(f, x1, y1, x2, y2)
        # Draw the North and West map border
        print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
        print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
        print('</svg>', file=f)


class Maze:
    def __init__(self, num_of_cells_x, num_of_cells_y, difficulty, operators, filename, start_cell_x=0, start_cell_y=0):
        self.num_of_cells_x, self.num_of_cells_y = num_of_cells_x, num_of_cells_y
        self.start_x, self.start_y = start_cell_x, start_cell_y
        self.maze_end = (self.num_of_cells_x - 1, self.num_of_cells_y - 1)
        self.maze = [[Cell(x, y, difficulty, operators) for y in range(num_of_cells_y)] for x in range(num_of_cells_x)]
        self.create_maze()
        self.set_cell_answers()
        write_map(self, filename)

    def get_cell(self, x: int, y: int):
        return self.maze[x][y]

    def set_cell_answers(self):
        for row in self.maze:
            for cell in row:
                for wall in cell.walls.values():
                    if not wall:
                        answer = eval(''.join(str(i) for i in cell.math_problem))
                        if answer % 1 != 0:
                            answer = round(answer, 3)
                    else:
                        answer = eval(''.join(str(i) for i in cell.math_problem)) + r.randrange(1, cell.settings['max_range'])
                        if answer % 1 != 0:
                            answer = round(answer, 3)

                    cell.answers.append(answer)

    def get_valid_neighbours(self, cell):
        """
        Checks the current cells neighbours by decrement or increment it's x and y value
        If the neighbouring cell is inside the map, it appends to the neighbour list
        :param cell: Cell instance, current cell
        :return: list
        """
        neighbours = []

        for direction, (direction_x, direction_y) in DIRECTIONS:
            neighbour_x, neighbour_y = cell.x + direction_x, cell.y + direction_y
            if 0 <= neighbour_x < self.num_of_cells_x and 0 <= neighbour_y < self.num_of_cells_y:
                neighbour = self.get_cell(neighbour_x, neighbour_y)
                if neighbour.surrounded_by_walls():
                    neighbours.append((direction, neighbour))

        return neighbours

    def create_maze(self):
        """
        The method checks the neighbouring cells and moves in random direction by removing the wall between the current
        and the next cell. If the neighbouring cell is a dead end, it backtracks to the last "unvisited" neighbour
        :return None
        """
        total_cells = self.num_of_cells_x * self.num_of_cells_y
        cell_stack = []
        current_cell = self.get_cell(self.start_x, self.start_y)
        created_cells = 1

        while created_cells < total_cells:
            neighbours = self.get_valid_neighbours(current_cell)

            if not neighbours:
                current_cell = cell_stack.pop()
                continue

            direction, next_cell = r.choice(neighbours)
            current_cell.remove_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            created_cells += 1


class Cell:
    WALL_SEPARATES = {
        'north': 'south',
        'south': 'north',
        'east': 'west',
        'west': 'east'
    }

    def __init__(self, x, y, difficulty, operator_list):
        self.x, self.y = x, y
        self.walls = {
            'north': True,
            'south': True,
            'east': True,
            'west': True
        }
        self.math_problem = None
        self.answers = []
        self.settings = difficulty_settings(difficulty)
        self.set_math_problem(operator_list)

    def set_math_problem(self, operator_list):

        def set_up():
            numbers = [r.randrange(1, self.settings['max_range']) for _ in range(r.choice(self.settings['numbers']))]
            operators = [r.choice(operator_list) for _ in range(len(numbers) - 1)]
            problem = [i for i in itertools.chain.from_iterable(itertools.zip_longest(numbers, operators)) if i is not None]
            ans = eval(''.join(str(i) for i in problem))
            return problem, ans

        self.math_problem, answer = set_up()

        if not self.settings['negative'] and not self.settings['decimals']:
            while answer < 0 or answer % 1 != 0:
                self.math_problem, answer = set_up()

        elif not self.settings['decimals']:
            while answer % 1 != 0:
                self.math_problem, answer = set_up()

    def surrounded_by_walls(self) -> bool:
        return all(self.walls.values())

    def remove_wall(self, other_cell, wall: str):
        """
        Method to remove the wall between two cells
        :param other_cell: Cell instance
        :param wall: str, the wall-direction to remove
        return: None
        """
        self.walls[wall] = False
        other_cell.walls[Cell.WALL_SEPARATES[wall]] = False
