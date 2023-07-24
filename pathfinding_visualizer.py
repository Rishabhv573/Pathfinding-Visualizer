import pygame
from queue import PriorityQueue
from heapq import heappop, heappush
from pygame.locals import *

# Initializing Pygame
pygame.init()

# Creating Pygame Window
WIDTH = 680
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Main Menu")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (100, 100, 255)
HIGHLIGHT_BLUE = (150, 150, 255)
BLACK = (0, 0, 0)
GREY = (220, 220, 220)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)


curr_pos = "main"

# Define font
font = pygame.font.SysFont("Proxima Nova", 30)

# Define navigation bar options
options = [
    "Dijkstra's Algorithm",
    "A* Algorithm"
]

# Define the choice of algorithm
algorithm_choice = None

# Loop to choose a algorithm
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the navigation bar area
            if 50 <= event.pos[0] <= WIDTH - 50 and 50 <= event.pos[1] <= WIDTH - 50:
                # Calculate the clicked option index based on the mouse position
                option_index = (event.pos[1] - 50) // 70  # Adjusted vertical spacing to 70 pixels

                # Check if the clicked option index is valid
                if 0 <= option_index < len(options):
                    algorithm_choice = option_index
                    running = False  # Exit the loop to proceed with the chosen algorithm

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Clear the window
    WIN.fill(GREY)

    # Draw the navigation bar
    for i, option in enumerate(options):
        option_rect = pygame.Rect(50, 50 + i * 70, WIDTH - 100, 50)  
        if option_rect.collidepoint(mouse_pos):
            pygame.draw.rect(WIN, HIGHLIGHT_BLUE, option_rect)
        elif i == algorithm_choice:
            pygame.draw.rect(WIN, LIGHT_BLUE, option_rect)
        else:
            pygame.draw.rect(WIN, BLUE, option_rect, 1)

        text_surface = font.render(option, True, BLUE)
        text_rect = text_surface.get_rect(center=option_rect.center)
        WIN.blit(text_surface, text_rect)

    pygame.display.update()

# Set the caption based on the selected option
if algorithm_choice is not None:
    pygame.display.set_caption(options[algorithm_choice])



class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = BLACK
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == WHITE

    def is_start(self):
        return self.color == YELLOW

    def is_end(self):
        return self.color == MAGENTA

    def reset(self):
        self.color = BLACK

    def make_start(self):
        self.color = YELLOW

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = WHITE

    def make_end(self):
        self.color = MAGENTA

    def make_path(self):
        self.color = CYAN

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        # DOWN
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


# heuristics function
def h(p1, p2): 
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# Reconstructing path from finish to end
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

#  ------------------------------------------ A* algorithm -----------------------------------------------
def a_star_algorithm(draw, grid, start, end):
    cnt = 0
    open_set = PriorityQueue()
    open_set.put((0, cnt, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + \
                    h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    cnt += 1
                    open_set.put((f_score[neighbor], cnt, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
#-------------------------------------------------------------------------------------------------------------

# ---------------------------------------- Dijkstra's Algorithm ----------------------------------------------
def dijkstra_algorithm(draw, grid, start, end):
    cnt = 0
    open_set = []
    heappush(open_set, (0, cnt, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = heappop(open_set)[2]

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score

                if neighbor not in open_set:
                    cnt += 1
                    heappush(open_set, (g_score[neighbor], cnt, neighbor))
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
#----------------------------------------------------------------------------------------------------------

# Function to make grid
def make_grid(rows, width): 
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def draw(win, grid, rows, width):
    win.fill(BLACK)

    for row in grid:
        for node in row:
            node.draw(win)

    gap = width // rows
    for i in range(rows): # From this loop we draw the grid lines
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

    pygame.display.update()


# To tell the coordinate where the user has clicked
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    i, j = pos

    row = i // gap
    col = j // gap

    return row, col


def main(win, width):
    ROWS = 40
    grid = make_grid(ROWS, width)

    start = None
    end = None
    run = True

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Loop will run until the user closes the game window
                run = False

            # When left mouse button is pressed
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()

            # When right mouse button is pressed
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:  # Start the algorithm when space bar is clicked
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    if algorithm_choice == 0:
                        dijkstra_algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    elif algorithm_choice == 1:
                        a_star_algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:  # Clear the grid upon pressing c
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

                if event.key == pygame.K_BACKSPACE:  # Get back to to the main window
                    if curr_pos != "main":
                        # Go back to the main position or top of the screen
                        curr_pos = "main"

    pygame.quit()


main(WIN, WIDTH)
